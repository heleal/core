from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords
from nltk.probability import FreqDist
import random
import string


class PreProcessing:

    def __init__(self, language) -> None:
        super().__init__()
        self.language = language

    def generate_tokens(self, comments):
        text = comments[0]
        mytkzr = TweetTokenizer()
        x = mytkzr.tokenize(text)
        return [x, comments[1]]

    def remove_stop_words(self, text):
        full_stop = self.remove_stop_words_full(text)
        return full_stop[0]

    def remove_stop_words_full(self, list_tokens_label):
        list_tokens = list_tokens_label[0]
        stop_words = set(stopwords.words(self.language))
        filtered_sentence = []
        stop_remove = []
        for token in list_tokens:
            w = token.lower()
            if w not in stop_words:
                filtered_sentence.append(w)
            else:
                stop_remove.append(w)
        return [filtered_sentence, stop_remove]

    def remove_punctuation(self, list_tokens_label):
        list_tokens = list_tokens_label[0]
        full_remove_punctuation = self.remove_punctuation_full(list_tokens)
        return [full_remove_punctuation[0], list_tokens_label[1]]

    def remove_punctuation_full(self, list_tokens_label):
        punctuation = string.punctuation
        filtered_sentence = []
        stop_remove = []
        list_tokens = list_tokens_label[0]

        for w in list_tokens:
            if w not in punctuation:
                filtered_sentence.append(w)
            else:
                stop_remove.append(w)
        return [filtered_sentence, stop_remove, list_tokens_label[1]]



