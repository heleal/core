from unittest import TestCase

from manipule_file.ImportData import ImportData
from preprocessamento.PreProcessing import PreProcessing
import os

from processamento.Processamento import Processamento
from testes.ConfTests import ConfTest


class TestProcessamento(TestCase):



    def setUp(self) -> None:
        super().setUpClass()

        s = ImportData()
        s = ImportData()
        base_folder = os.path.realpath(ConfTest.FOLDER_DATA)
        file = "IMDb-sample_01.csv"
        path_file = os.path.join(base_folder, file)
        lista = s.read_csv_file(path_file)


        self.limite = 100

        self.pree_processamento = PreProcessing()
        self.processamento = Processamento()

        sub_lista = lista[:self.limite]
        self.lista = sub_lista

    def test_processa_text_blog(self):
        for texto in self.lista:
            resultado = self.processamento.processa_text_blob(texto)
            print(resultado)

    def test_get_word_freq(self):
        sub_lista = self.lista
        frequencia = self.processamento.get_word_freq(sub_lista)
        print(frequencia.most_common(10))

