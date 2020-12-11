from unittest import TestCase

from importa_arquivo.Learquivo import Learquivo
import os

class TestLearquivo(TestCase):

    def test_acessaarquivo(self):
        s = Learquivo()
        pai = os.path.abspath("D:\\faculdade\\Text Minning\\Dados")
        arquivo = "IMDb-sample_01.csv"
        caminho = os.path.join(pai,arquivo)
        print(caminho)
        lista = s.acessaarquivo(caminho)
        print("ola mindo")
        # print(lista[:100])
        for docs in lista[:100]:
            print(docs)

    def test_ler_arquivo_json(self):
        s = Learquivo()
        pai = os.path.abspath("D:\\faculdade\\Text Minning\\Dados")
        arquivo = "SFU_Review_Corpus.json"
        arquivo = "IMDb-sample.json"
        caminho = os.path.join(pai,arquivo)

        lista = s.lerArquivoJson(caminho)

        # print(lista[:100])
        for docs in lista[:100]:
            print(docs)
