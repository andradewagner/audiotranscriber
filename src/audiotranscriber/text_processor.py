import nltk
import spacy
import yaml
from audiotranscriber.logger_config import get_logger

nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("stopwords")

from audiotranscriber.nlp.nltk_tokenizer import NLTKTokenizer
from audiotranscriber.nlp.preprocessor import Preprocessor
from audiotranscriber.nlp.spacy_tokenizer import SpacyTokenizer

class TextProcessorPipeline:
    def __init__(self, config, logger, tokenizer, preprocessor=None, spacy_tokenizer=None, embedder=None, vector_store=None):
        self.config = config
        self.logger = logger
        self.tokenizer = tokenizer
        self.preprocessor = preprocessor
        self.spacy_tokenizer = spacy_tokenizer
        self.embedder = embedder
        self.vector_store = vector_store

    def load_text(self):
        file_path = self.config["audio"]["transcriptions_path"]
        self.logger.info(f"Loading text file from: {file_path}")

        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()

    def run(self):
        self.logger.info("Starting text processing pipeline...")
        text = self.load_text()

        # Pré-processamento
        preprocessed_text = self.preprocessor.preprocess(text)
        self.logger.info(f"Text loaded. First 100 characters: {preprocessed_text[:100]}")
        return preprocessed_text

def run_text_processing(config_path: str = "config.yaml"):
    config = yaml.safe_load(open(config_path))
    logger = get_logger("pipeline", config)

    tp = config["text_processing"]

    spacy_tokenizer = SpacyTokenizer(model_name=tp["spacy"]["model_name"])

    preprocessor = Preprocessor(
        lowercase=True,
        remove_accents=True,
        remove_special=True,
        remove_stopwords=tp["remove_stopwords"],
        stemming=tp["stemming"],
        lemmatization=tp["lemmatization"],
        stemmer_type=tp["stemmer_type"],
        language=tp["tokenizer_language"],
        spacy_nlp=spacy_tokenizer.nlp
    )

    tokenizer = NLTKTokenizer(language=config["text_processing"]["tokenizer_language"])

    pipeline = TextProcessorPipeline(
        config=config,
        logger=logger,
        tokenizer=tokenizer,
        preprocessor=preprocessor,
        spacy_tokenizer=spacy_tokenizer
    )

    return pipeline.run()
