from unittest import TestCase

from importa_arquivo.Learquivo import Learquivo
import os

from preprocessamento.Preprocessamento import Preprocessamento


class TestPreprocessamento(TestCase):



    @classmethod
    def setUpClass(self) -> None:
        super().setUpClass()

        s = Learquivo()
        pai = os.path.abspath("D:\\faculdade\\Text Minning\\Dados")
        arquivo = "IMDb-sample_01.csv"
        caminho = os.path.join(pai, arquivo)
        print(caminho)
        lista = s.acessaarquivo(caminho)
        self.lista = lista

        self.limite = 100

        self.preeprocessamento = Preprocessamento()

    def test_gera_token(self):
        for comentario in self.lista[:self.limite]:
            tokens = self.preeprocessamento.gera_token(comentario)
            print(tokens)