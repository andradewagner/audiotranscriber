import nltk
import spacy
import yaml
from logger_config import get_logger

nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("stopwords")

from nlp.nltk_tokenizer import NLTKTokenizer
from nlp.preprocessor import Preprocessor
from nlp.spacy_tokenizer import SpacyTokenizer

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

        self.logger.info(f"Text loaded. First 100 characters: {text[:100]}")

        # Pré-processamento
        normalized_text = self.preprocessor.preprocess(text)

        # Tokenização NLTK
        sentences = self.tokenizer.tokenize_sentences(normalized_text)

        # spaCy
        print("Texto com spaCy:")
        print(self.spacy_tokenizer.process_text(text))
        print(self.spacy_tokenizer.tokenize_words(text))
        print("*" * 100)

        self.logger.info(f"Found {len(sentences)} sentences.")

        return sentences

if __name__ == "__main__":
    config = yaml.safe_load(open("config.yaml"))
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
    spacy_tokenizer = SpacyTokenizer(model_name=config["text_processing"]["spacy"]["model_name"])

    pipeline = TextProcessorPipeline(
        config=config,
        logger=logger,
        tokenizer=tokenizer,
        preprocessor=preprocessor,
        spacy_tokenizer=spacy_tokenizer
    )

    resultado = pipeline.run()
    print(f"Resultado: {resultado[:5]}")
