from unittest import TestCase

from manipule_file.ImportData import ImportData
import os

from testes.ConfTests import ConfTest


class TestLearquivo(TestCase):



    def setUp(self) -> None:
        super().setUp()
        self.limit = 100


    def test_acessaarquivo(self):
        s = ImportData()
        pai = os.path.abspath("D:\\faculdade\\Text Minning\\Dados")
        arquivo = "IMDb-sample_01.csv"
        caminho = os.path.join(pai,arquivo)
        print(caminho)
        lista = s.read_csv_file(caminho)
        # print(lista[:100])
        for docs in lista[:100]:
            print(docs)

    def test_acessaarquivo_conf(self):
        s = ImportData()
        base_folder = os.path.realpath(ConfTest.FOLDER_DATA)
        print(base_folder)
        file = "IMDb-sample_01.csv"
        path_file = os.path.join(base_folder, file)
        print(path_file)
        lista = s.read_csv_file(path_file)
        for docs in lista[:self.limit]:
            print(docs)

    def test_ler_arquivo_json(self):
        s = ImportData()
        base_folder = os.path.realpath(ConfTest.FOLDER_DATA)
        print(base_folder)
        file = "IMDb-sample.json"
        path_file = os.path.join(base_folder, file)
        lista = s.read_json(path_file)
        for docs in lista[:100]:
            print(docs)



    def test_read_folder_csv(self):
        path_folder = os.path.realpath(ConfTest.FOLDER_DATA_NEG)
        s = ImportData()
        neg = s.read_folder_csv(path_folder, 100, "NEG", False)

        path_folder = os.path.realpath(ConfTest.FOLDER_DATA_POS)
        pos = s.read_folder_csv(path_folder, 100, "POS", False)
        print("sdas")

    def test_read_folder_csv_random(self):
        path_folder = os.path.realpath(ConfTest.FOLDER_DATA_NEG)
        s = ImportData()
        neg01 = s.read_folder_csv(path_folder, 10, "NEG", True)
        neg02 = s.read_folder_csv(path_folder, 10, "NEG", True)
        neg03 = s.read_folder_csv(path_folder, 10, "NEG", True)
        print("dfsd")