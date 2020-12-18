import numpy
import pandas as pd
import matplotlib.pyplot as plt
import nltk
import seaborn as sns
#pip install numpy==1.19.3
import unidecode
#nltk.download("all")

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer # bag of words
from sklearn.feature_extraction.text import TfidfVectorizer
from wordcloud import WordCloud #matlab
from nltk import tokenize
from nltk import ngrams
from string import punctuation


class SalaEmpreendedor:

    def inicializa_dados(self, path_file):
        uri = path_file
        resenha = pd.read_csv(uri, sep=";")

        mapa = {"Descrição": "Descricao",
                "Ação": "Acao",
                "Início do Atendimento": "Ini_Atend",
                "Fim do Atendimento	": "Fim_Atend"}
        dados = resenha.rename(columns=mapa)

        # print(dados.Instrumento.value_counts())
        dados.head()

        classificacao = dados["Instrumento"].replace(["Orientação Técnica Presencial",
                                                      "Informação Presencial",
                                                      "Orientação Técnica a Distância",
                                                      "Consultoria Presencial",
                                                      "Informação a Distância"], [0, 1, 2, 3, 4])
        dados["Classificacao"] = classificacao
        return dados

    def classificacar_texto(self,texto, col_texto, col_classificacao):
        # vetorizar = CountVectorizer(lowercase=False, max_features=50) # limita o vetor
        # bag_of_words = vetorizar.fit_transform(texto[col_texto])

        # TF-IDF
        tfidf = TfidfVectorizer(lowercase=False, ngram_range=(1, 2))  # ngrams 2
        bag_of_words = tfidf.fit_transform(texto[col_texto])

        treino, teste, classe_treino, classe_teste = train_test_split(bag_of_words,
                                                                      texto[col_classificacao],
                                                                      random_state=122)

        regressao_logistica = LogisticRegression(solver="lbfgs")
        regressao_logistica.fit(treino, classe_treino)

        return regressao_logistica.score(teste, classe_teste)

    def gera_list_pontos(self):
        pontuacao = list()  # lista de pontuacao
        for ponto in punctuation:
            pontuacao.append(ponto)
        pontuacao.append("DA")
        pontuacao.append("DE")
        pontuacao.append("DO")
        pontuacao.append("E")
        pontuacao.append("A")
        pontuacao.append("PARA")
        pontuacao.append("•")

        return pontuacao

    def gera_list_irrelevantes(self, list_pontuacao):
        palavras_irrelevantes = nltk.corpus.stopwords.words("portuguese") # palavras irrelevantes
        pontuacao_stopwords = list_pontuacao + palavras_irrelevantes
        return pontuacao_stopwords

    def limpa_dados(self, dados, pontuacao_stopwords):
        frase_processada = list()
        token_espaco = tokenize.WhitespaceTokenizer()

        for opiniao in dados.Descricao:
            nova_frase = list()
            palavra_texto = token_espaco.tokenize(opiniao)  # tokenizar
            for palavra in palavra_texto:  # para cada palavra da frase tokenizada
                if palavra not in pontuacao_stopwords:
                    nova_frase.append(palavra)  # forma a nova frase como uma lista
            frase_processada.append(' '.join(nova_frase))  # monta a string
        return frase_processada

    # nuvem_palavras
    def nuvem_palavras_graf(self, texto, pesquisa, dados):

        # txt_ori_tec_p = texto.query("Instrumento=='"+pesquisa+"'")

        todas_palavras = ''.join([texto for texto in dados.tratamento_1])
        nuvem_palavras = WordCloud(width=800,
                                   height=500,
                                   max_font_size=110,
                                   collocations=False).generate(todas_palavras)
        # gerar o grafico
        plt.figure(figsize=(10, 7))
        plt.imshow(nuvem_palavras, interpolation="bilinear")
        plt.axis("off")
        plt.title(pesquisa)
        plt.show()

    def cria_nuvens(self, dados):
        self.nuvem_palavras_graf(dados, "Orientação Técnica Presencial")
        self.nuvem_palavras_graf(dados, "Informação Presencial")
        self.nuvem_palavras_graf(dados, "Orientação Técnica a Distância")
        self.nuvem_palavras_graf(dados, "Consultoria Presencial")
        self.nuvem_palavras_graf(dados, "Informação a Distância")

    def tokeniza_data_set(self, dados):
        # Tokenizar o Dataset
        todas_palavras = ''.join([texto for texto in dados.tratamento_1])
        token_espaco = tokenize.WhitespaceTokenizer()

        token_frase = token_espaco.tokenize(todas_palavras)  # toda a base lá de cima
        frequencia = nltk.FreqDist(token_frase)
        return frequencia

    def cria_data_frame_frequencia(self, frequencia):
        # criar um dataframe com a frequencia

        df_frequencia = pd.DataFrame({"Palavra": list(frequencia.keys()),
                                      "Frequencia": list(frequencia.values()
                                                         )})
        df_frequencia.nlargest(columns="Frequencia", n=20)  # 20 mais frequentes

    # Pareto - criação e exploração

    def pareto(self, texto, coluna_texto, qtd):
        todas_palavras = ''.join([texto for texto in texto[coluna_texto]])
        token_espaco = tokenize.WhitespaceTokenizer()
        token_frase = token_espaco.tokenize(todas_palavras)  # toda a base lá de cima

        frequencia = nltk.FreqDist(token_frase)
        # criar um dataframe com a frequencia
        df_frequencia = pd.DataFrame({"Palavra": list(frequencia.keys()),
                                      "Frequencia": list(frequencia.values())
                                      })
        df = df_frequencia.nlargest(columns="Frequencia", n=qtd)
        plt.figure(figsize=(12, 8))
        ax = sns.barplot(data=df, x="Palavra", y="Frequencia", color="grey")  # mostra as frequencais
        ax.set(ylabel="Contagem")
        plt.show()

    def exec_01(self, path_file):
        dados = self.inicializa_dados(path_file)
        self.pareto(dados, "tratamento_1", 10)
        acuracia_tratamento = self.classificacar_texto(dados, "tratamento_1", "Classificacao")
        print(acuracia_tratamento)
        # frase_separada = token_espaco.tokenize(dados.tratamento_1[2064]) # frase tokenizada
        # pares = ngrams(frase_separada, 2) # manter a sequencia de duas palavras
        # list(pares)