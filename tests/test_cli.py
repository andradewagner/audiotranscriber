import pytest
from typer.testing import CliRunner
from unittest.mock import patch, MagicMock

from audiotranscriber.cli import app

runner = CliRunner()


def test_cli_help():
    """Verifica se o comando --help funciona."""
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "Usage" in result.stdout or "Uso" in result.stdout


def test_cli_transcribe_missing_argument():
    """Se o usuário não passar o arquivo, deve falhar."""
    result = runner.invoke(app, ["transcribe"])
    assert result.exit_code != 0
    assert "Error" in result.stdout or "erro" in result.stdout.lower()


def test_cli_transcribe_calls_transcriber():
    """Garante que o CLI chama o AudioTranscriber corretamente."""
    with patch("audiotranscriber.cli.AudioTranscriber") as mock_transcriber:
        instance = MagicMock()
        instance.transcribe.return_value = "texto transcrito"
        mock_transcriber.return_value = instance

        result = runner.invoke(app, ["transcribe", "audio_fake.wav"])

        assert result.exit_code == 0
        instance.transcribe.assert_called_once_with("audio_fake.wav")
        assert "texto transcrito" in result.stdout


def test_cli_transcribe_file_not_found():
    """Se o arquivo não existir, o CLI deve exibir erro amigável."""
    with patch("audiotranscriber.cli.AudioTranscriber") as mock_transcriber:
        instance = MagicMock()
        instance.transcribe.side_effect = FileNotFoundError("Arquivo não encontrado")
        mock_transcriber.return_value = instance

        result = runner.invoke(app, ["transcribe", "inexistente.wav"])

        assert result.exit_code != 0
        assert "não encontrado" in result.stdout.lower()


def test_cli_transcribe_with_model_option():
    """Testa se a flag --model é passada corretamente."""
    with patch("audiotranscriber.cli.AudioTranscriber") as mock_transcriber:
        instance = MagicMock()
        instance.transcribe.return_value = "ok"
        mock_transcriber.return_value = instance

        result = runner.invoke(app, ["transcribe", "audio.wav", "--model", "tiny"])

        assert result.exit_code == 0
        mock_transcriber.assert_called_once_with(model_name="tiny", language=None)