import os
import whisper
import yaml
import time
from typing import Dict, Any
from audiotranscriber.logger_config import get_logger

class AudioTranscriberPipeline:
    def __init__(self, config_path: str = "config.yaml"):
        """Inicia o pipeline, carrega configurações e configura o logger."""
        self.config_path = config_path
        self.config = self._load_config()
        self.logger = get_logger(__name__, self.config)

    def _load_config(self) -> Dict[str, Any]:
        """Carrega as configurações do arquivo YAML."""
        try:
            with open(self.config_path, "r") as f:
                config = yaml.safe_load(f)
            print(f"Configuration loaded successfully from {self.config_path}")
            return config
        except Exception as e:
            print(f"Failed to load configuration from {self.config_path}: {str(e)}")
            raise

    def load_audio(self) -> Any: 
        """Carrega o arquivo de áudio especificado na configuração."""
        start_load = time.perf_counter()
        
        file_path = self.config["audio"]["audio_path"]
        self.logger.info(f"Loading audio file from: {file_path}")
        
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Audio file not found at: {file_path}")
            
        audio = whisper.load_audio(file_path)
        
        end_load = time.perf_counter()
        self.logger.info(f"Audio loaded in {end_load - start_load:.2f} seconds.")
        return audio

    def transcribe_audio(self) -> str:
        """Carrega o modelo Whisper dinâmico e transcreve o áudio."""
        audio = self.load_audio()
        
        model_name = self.config["whisper"].get("model", "base")
        
        self.logger.info(f"Loading Whisper model ('{model_name}')...")
        start_model = time.perf_counter()
        model = whisper.load_model(model_name)
        end_model = time.perf_counter()
        self.logger.info(f"Model loaded in {end_model - start_model:.2f} seconds.")

        self.logger.info("Starting audio transcription...")
        start_transcribe = time.perf_counter()
        
        # Parâmetros adicionados para evitar alucinações e travamentos no modelo Turbo
        result = model.transcribe(
            audio,
            temperature=0.0,
            no_speech_threshold=0.6,
            logprob_threshold=-1.0,
            condition_on_previous_text=False
        )
        
        end_transcribe = time.perf_counter()
        self.logger.info(f"Transcription completed in {end_transcribe - start_transcribe:.2f} seconds.")
        
        texto_formatado = ""
        fim_ultimo_segmento = 0.0

        for segment in result["segments"]:
            # Se a pausa entre o fim da última frase e o início desta for maior que 2.0 segundos
            if segment["start"] - fim_ultimo_segmento > 2.0:
                texto_formatado += "\n\n"  # Cria um novo parágrafo
            else:
                texto_formatado += " "  # Apenas continua na mesma linha
                
            texto_formatado += segment["text"].strip()
            fim_ultimo_segmento = segment["end"]

        # Corrigido: Retorna a string estruturada com parágrafos em vez do texto bruto em uma linha só
        return texto_formatado.strip()

    def save_transcription(self, transcription: str) -> None:
        """Salva o texto no arquivo de saída configurado."""
        transcriptions_path = self.config["audio"]["transcriptions_path"]
        
        os.makedirs(os.path.dirname(transcriptions_path), exist_ok=True)

        self.logger.info(f"Saving transcription text to: {transcriptions_path}")
        with open(transcriptions_path, "w", encoding="utf-8") as f:
            f.write(transcription)

    def run(self) -> None:
        """Executa o pipeline completo de transcrição com checagem antecipada."""
        try:
            # --- Validação Antecipada (Fail-Fast) ---
            transcriptions_path = self.config["audio"]["transcriptions_path"]
            overwrite = self.config["audio"].get("overwrite_transcriptions", False)
            
            if os.path.exists(transcriptions_path) and not overwrite:
                msg = (
                    "flag de overwrite igual a false, mude a flag, "
                    "renomeie ou apague o arquivo de saída na pasta processed"
                )
                self.logger.error(msg)
                return  # Interrompe a execução imediatamente sem gastar processamento
            # ----------------------------------------

            start_total = time.perf_counter()
            self.logger.info(f"Starting pipeline for project: {self.config.get('project_name')}")
            self.logger.info(f"Experiment: {self.config.get('experiment_name')}")

            transcription = self.transcribe_audio()
            self.save_transcription(transcription)

            end_total = time.perf_counter()
            total_seconds = end_total - start_total

            minutes = int(total_seconds // 60)
            seconds = total_seconds % 60

            self.logger.info("Process finished successfully!")
            self.logger.info(f"Total time taken: {minutes}m {seconds:.2f}s ({total_seconds:.4f} seconds)")

        except Exception as e:
            self.logger.error(f"An error occurred during execution: {str(e)}", exc_info=True)
            raise

def run_transcription(config_path: str = "config.yaml"):
    pipeline = AudioTranscriberPipeline(config_path="config.yaml")
    pipeline.run()