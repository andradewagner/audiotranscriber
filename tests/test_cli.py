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
    assert "Missing argument" in result.stderr or "argumento" in result.stderr.lower()


def test_cli_transcribe_calls_transcriber():
    """Garante que o CLI chama run_transcription corretamente."""
    with patch("audiotranscriber.cli.run_transcription") as mock_run:
        result = runner.invoke(app, ["transcribe", "audio_fake.wav"])

        assert result.exit_code == 0
        mock_run.assert_called_once()


def test_cli_transcribe_file_not_found():
    """O CLI deve chamar run_transcription mesmo se o arquivo não existir,
    pois ele não valida o caminho do áudio."""
    with patch("audiotranscriber.cli.run_transcription") as mock_run:
        result = runner.invoke(app, ["transcribe", "inexistente.wav"])

        assert result.exit_code == 0
        mock_run.assert_called_once()
