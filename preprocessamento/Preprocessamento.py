from nltk.tokenize import TweetTokenizer
class Preprocessamento:

    def gera_token(self,texto):
        mytkzr = TweetTokenizer()
        x = mytkzr.tokenize(texto)
        return x