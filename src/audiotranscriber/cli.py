import typer
import yaml
from audiotranscriber.transcriber import run_transcription
from audiotranscriber.text_processor import run_text_processing

app = typer.Typer(help="AudioTranscriber CLI")

@app.command()
def transcribe(
    audio: str = typer.Argument(..., help="Caminho do arquivo de áudio"),
    config: str = typer.Option("config.yaml", help="Arquivo de configuração")
    ):
    """
    Roda a transcrição usando o arquivo de configuração.
    """

    # Atualiza o caminho do áudio no config.yaml
    with open(config, "r") as f:
        cfg = yaml.safe_load(f)

    cfg["audio"]["audio_path"] = audio

    with open(config, "w") as f:
        yaml.safe_dump(cfg, f)

    run_transcription(config)

@app.command()
def process(text_file: str, config: str = "config.yaml"):

    with open(config, "r") as f:
        cfg = yaml.safe_load(f)

    # Atualiza o caminho do texto no config
    cfg["audio"]["transcriptions_path"] = text_file

    with open(config, "w") as f:
        yaml.safe_dump(cfg, f)

    run_text_processing(config)


def main():
    app()