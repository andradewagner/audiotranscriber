class Vectorize:
    def __init__ (
            self, 
            method="tfidf", 
            max_features=5000, 
            ngram_range=(1,1)):
        self.method = method
        self.max_features = max_features
        self.ngram_range = ngram_range
        self.vectorizer = None

    def fit_transform(self, texts):
        if self.method == "bow":
            from sklearn.feature_extraction.text import CountVectorizer
            self.vectorizer = CountVectorizer(
                max_features=self.max_features,
                ngram_range=self.ngram_range
            )
        elif self.method == "tfidf":
            from sklearn.feature_extraction.text import TfidfVectorizer
            self.vectorizer = TfidfVectorizer(
                max_features=self.max_features,
                ngram_range=self.ngram_range
            )
        elif self.method == "embeddings":
            pass

        return self.vectorizer.fit_transform(texts)
    
    def transform(self, texts):
        return self.vectorizer.transform(texts)
    
    def get_words(self):
        return self.vectorizer.get_feature_names_out()