import pytest
from unittest.mock import patch, MagicMock
from audiotranscriber.transcriber import AudioTranscriberPipeline


def test_import_transcriber():
    """Verifica se o módulo importa corretamente."""
    from audiotranscriber.transcriber import AudioTranscriberPipeline
    assert AudioTranscriberPipeline is not None