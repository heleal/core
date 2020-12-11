from unittest import TestCase

from importa_arquivo.Learquivo import Learquivo
from preprocessamento.Preprocessamento import Preprocessamento
import os

from processamento.Processamento import Processamento


class TestProcessamento(TestCase):



    def setUp(self) -> None:
        super().setUpClass()

        s = Learquivo()
        pai = os.path.abspath("D:\\faculdade\\Text Minning\\Dados")
        arquivo = "IMDb-sample_01.csv"
        caminho = os.path.join(pai, arquivo)
        print(caminho)
        lista = s.acessaarquivo(caminho)


        self.limite = 100

        self.pree_processamento = Preprocessamento()
        self.processamento = Processamento()

        sub_lista = lista[:self.limite]
        self.lista = sub_lista

    def test_processa_text_blog(self):
        for texto in self.lista:
            resultado = self.processamento.processa_text_blob(texto)
            print(resultado)

    def test_get_word_freq(self):
        sub_lista = self.lista[:5]
        frequencia = self.processamento.get_word_freq(sub_lista)
        print(frequencia.most_common(10))
