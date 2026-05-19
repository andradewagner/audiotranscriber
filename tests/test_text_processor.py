import pytest
from unittest.mock import patch, MagicMock
from audiotranscriber.text_processor import TextProcessor


def test_import_text_processor():
    """Verifica se o módulo importa corretamente."""
    from audiotranscriber.text_processor import TextProcessor
    assert TextProcessor is not None


def test_processor_initialization():
    """Testa se a classe inicializa com valores padrão."""
    processor = TextProcessor()
    assert processor.language == "portuguese"
    assert processor.enable_stemming is True
    assert processor.enable_lemmatization is True


def test_normalize_text():
    """Testa a normalização básica."""
    processor = TextProcessor()
    text = "Olá, Mundo! 123"
    normalized = processor.normalize(text)
    assert normalized == "olá mundo 123"


def test_remove_stopwords():
    """Testa remoção de stopwords usando mock do NLTK."""
    processor = TextProcessor()

    with patch("audiotranscriber.text_processor.stopwords.words", return_value=["de", "a", "o"]):
        result = processor.remove_stopwords("gosto de programar a noite")
        assert result == "gosto programar noite"


def test_stemming():
    """Testa stemming usando mock do NLTK."""
    processor = TextProcessor()

    mock_stemmer = MagicMock()
    mock_stemmer.stem.side_effect = lambda w: w[:-1]  # simula um stemmer simples

    with patch("audiotranscriber.text_processor.SnowballStemmer", return_value=mock_stemmer):
        result = processor.apply_stemming("programando testes automáticos")
        assert result == "programand teste automático"


def test_lemmatization():
    """Testa lematização usando mock do spaCy."""
    processor = TextProcessor()

    mock_token = MagicMock()
    mock_token.lemma_ = "correr"

    mock_nlp = MagicMock()
    mock_nlp.return_value = [mock_token]

    with patch("audiotranscriber.text_processor.spacy.load", return_value=mock_nlp):
        result = processor.apply_lemmatization("correndo")
        assert result == "correr"


def test_full_pipeline():
    """Testa a pipeline completa com mocks."""
    processor = TextProcessor()

    with patch("audiotranscriber.text_processor.stopwords.words", return_value=["de"]):
        with patch("audiotranscriber.text_processor.SnowballStemmer") as mock_stem:
            stemmer = MagicMock()
            stemmer.stem.side_effect = lambda w: w  # não altera
            mock_stem.return_value = stemmer

            with patch("audiotranscriber.text_processor.spacy.load") as mock_spacy:
                mock_token = MagicMock()
                mock_token.lemma_ = "teste"
                mock_spacy.return_value = lambda x: [mock_token]

                result = processor.process("Testando de novo")
                assert isinstance(result, str)
                assert "teste" in result