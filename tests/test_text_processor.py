import pytest
from unittest.mock import patch, MagicMock
from audiotranscriber.text_processor import TextProcessorPipeline


def test_import_text_processor():
    """Verifica se o módulo importa corretamente."""
    from audiotranscriber.text_processor import TextProcessorPipeline
    assert TextProcessorPipeline is not None


def test_processor_initialization():
    """Testa se a classe inicializa com valores fornecidos."""
    mock_config = {"language": "pt"}
    mock_logger = MagicMock()
    mock_tokenizer = MagicMock()

    processor = TextProcessorPipeline(
        config=mock_config,
        logger=mock_logger,
        tokenizer=mock_tokenizer
    )

    assert processor.config == mock_config
    assert processor.logger == mock_logger
    assert processor.tokenizer == mock_tokenizer



def test_text_processing():
    """Testa a normalização básica."""
    mock_config = {"language": "pt"}
    mock_logger = MagicMock()
    mock_tokenizer = MagicMock()

    processor = TextProcessorPipeline(
        config=mock_config,
        logger=mock_logger,
        tokenizer=mock_tokenizer
    )

    normalized = processor.run_text_processing()
    assert normalized is not None