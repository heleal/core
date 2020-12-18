import nltk
from nltk import FreqDist
from textblob import TextBlob
from nltk.classify import NaiveBayesClassifier as nbc
#positive NaiveBayes
import random

class Processing:

    def __init__(self, language, seed=None) -> None:
        super().__init__()
        if(seed!=None):
            random.seed(seed)
        self.language = language

    def processa_text_blob(self, linha):
        texts = []
        text = TextBlob(linha)
        sentencas = text.sentences
        for s in sentencas:
            sentimento = s.sentiment
            polaridade = sentimento[0]
            subjetividade = sentimento[1]
            texts.append([s.raw, polaridade, subjetividade])
        return texts

    def separate_train_and_test_tokens(self, list_comment,sp):
        a = list_comment[:sp]
        b = list_comment[sp:]
        return [a, b]

    def find_freq_dist(self, abc):
        word_freq = FreqDist()
        for tokens in abc:
            word_freq += FreqDist(token for token in tokens)
        return word_freq

    def create_features(self, documents):
        doc_rep = []
        for words in documents:
            features = FreqDist(w.lower() for w in words)
            doc_rep.append([features, "POS"])
        return doc_rep

    def train_naive(self, doc_rep_train, doc_rep_test):
        classifier = nbc.train(doc_rep_train)
        acur = nltk.classify.accuracy(classifier, doc_rep_test)
        print(acur)
        return classifier