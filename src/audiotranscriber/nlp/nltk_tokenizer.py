from nltk.tokenize import word_tokenize, sent_tokenize, casual_tokenize
from typing import List

class NLTKTokenizer:
    def __init__(self, language: str = "english"):
        self.language = language

    def tokenize_sentences(self, text: str) -> List[str]:
        return sent_tokenize(text, language=self.language)

    def tokenize_words(self, text: str) -> List[str]:
        return word_tokenize(text, language=self.language)

    def tokenize_casual(self, text: str) -> List[str]:
        return casual_tokenize(text, language=self.language)