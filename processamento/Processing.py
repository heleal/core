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
        num_train = int(len(list_comment) * sp/100)
        list_train = list_comment[:num_train]
        list_set = list_comment[num_train:]
        return [list_train, list_set]


    def create_features(self, documents):
        doc_rep = []
        for words, tag in documents:
            features = FreqDist(w.lower() for w in words)
            doc_rep.append([features, tag])
        return doc_rep

    def train_naive(self, doc_rep_train, doc_rep_test):
        classifier = nbc.train(doc_rep_train)
        acur = nltk.classify.accuracy(classifier, doc_rep_test)
        print(acur)
        print(classifier.show_most_informative_features(10))
        return classifier