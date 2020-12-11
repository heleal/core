from textblob import TextBlob
from nltk.probability import FreqDist


class Processamento:

    def processa_text_blob(self, linha):
        texts = []
        text = TextBlob(linha)
        sentensas = text.sentences
        for s in sentensas:
            sentimento = s.sentiment
            polaridade = sentimento[0]
            subjetividade = sentimento[1]
            texts.append([s.raw, polaridade, subjetividade])
        return texts

    def get_word_freq(self, textos):
        wordfreq = FreqDist()
        for i in textos:
            wordfreq += FreqDist(w.lower() for w in i.split())
        return wordfreq

