import spacy

class SpacyTokenizer:
    def __init__(self, model_name="pt_core_news_md"):
        self.nlp = spacy.load(model_name)

    def process_text(self, text: str):
        return self.nlp(text)
    
    def tokenize_sentences(self, text: str):
        doc = self.nlp(text)
        return [sent.text for sent in doc.sents]
    
    def tokenize_words(self, text: str):
        doc = self.nlp(text)

        data = []
        for token in doc:
            data.append({
                "token": token,
                "Punctuation": token.is_punct,
                "Space": token.is_space,
                "Alpha": token.is_alpha,
                "Shape": token.shape_
            })
        print(data)
        return [token.text for token in doc]