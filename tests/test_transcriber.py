import pytest
from unittest.mock import patch, MagicMock
from audiotranscriber.transcriber import AudioTranscriberPipeline


def test_import_transcriber():
    """Verifica se o módulo importa corretamente."""
    from audiotranscriber.transcriber import AudioTranscriberPipeline
    assert AudioTranscriberPipeline is not None


def test_transcriber_initialization():
    """Testa se a classe inicializa com os parâmetros padrão."""
    transcriber = AudioTranscriberPipeline()
    assert transcriber.model_name == "base"
    assert transcriber.language is None


def test_transcriber_load_model_called():
    """Garante que o modelo Whisper é carregado ao inicializar."""
    with patch("audiotranscriber.transcriber.whisper.load_model") as mock_load:
        AudioTranscriberPipeline(model_name="tiny")
        mock_load.assert_called_once_with("tiny")


def test_transcribe_file_not_found():
    """Se o arquivo não existe, deve levantar FileNotFoundError."""
    transcriber = AudioTranscriberPipeline()

    with pytest.raises(FileNotFoundError):
        transcriber.transcribe("arquivo_inexistente.wav")


def test_transcribe_calls_whisper():
    """Garante que o método transcribe chama o modelo Whisper corretamente."""
    mock_model = MagicMock()
    mock_model.transcribe.return_value = {"text": "teste transcrição"}

    with patch("audiotranscriber.transcriber.whisper.load_model", return_value=mock_model):
        transcriber = AudioTranscriberPipeline()
        result = transcriber.transcribe("audio_fake.wav")

    mock_model.transcribe.assert_called_once()
    assert result == "teste transcrição"


def test_transcribe_returns_string():
    """Garante que o retorno é sempre uma string."""
    mock_model = MagicMock()
    mock_model.transcribe.return_value = {"text": "conteúdo"}

    with patch("audiotranscriber.transcriber.whisper.load_model", return_value=mock_model):
        transcriber = AudioTranscriberPipeline()
        output = transcriber.transcribe("audio_fake.wav")

    assert isinstance(output, str)