import unicodedata
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, SnowballStemmer

class Preprocessor:
    def __init__(
        self,
        lowercase=True,
        remove_accents=False,
        remove_special=False,
        remove_stopwords=False,
        stemming=False,
        lemmatization=False,
        stemmer_type="snowball",
        language="portuguese",
        spacy_nlp=None
    ):
        self.lowercase = lowercase
        self.remove_accents = remove_accents
        self.remove_special = remove_special
        self.remove_stopwords = remove_stopwords
        self.stemming = stemming
        self.lemmatization = lemmatization
        self.language = language
        self.stemmer_type = stemmer_type
        self.spacy_nlp = spacy_nlp

        if remove_stopwords:
            self.stopwords = set(stopwords.words(language))

        if stemming:
            if stemmer_type == "porter":
                self.stemmer = PorterStemmer()
            else:
                self.stemmer = SnowballStemmer(language)

    @staticmethod
    def normalize_unicode(text: str, form: str = "NFC") -> str:
        return unicodedata.normalize(form, text)

    @staticmethod
    def case_fold(text: str) -> str:
        return text.casefold()

    def preprocess(self, text: str) -> str:
        text = self.normalize_unicode(text)

        if self.lowercase:
            text = self.case_fold(text)

        if self.remove_accents:
            text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("utf-8")

        if self.remove_special:
            text = re.sub(r"[^a-zA-Z0-9\s]", " ", text)

        tokens = word_tokenize(text)

        if self.remove_stopwords:
            tokens = [t for t in tokens if t not in self.stopwords]

        if self.stemming:
            tokens = [self.stemmer.stem(t) for t in tokens]

        # LEMATIZAÇÃO COM SPACY
        if self.lemmatization and self.spacy_nlp:
            doc = self.spacy_nlp(" ".join(tokens))
            tokens = [token.lemma_ for token in doc]

        text = " ".join(tokens)
        text = re.sub(r"\s+", " ", text).strip()

        return text
