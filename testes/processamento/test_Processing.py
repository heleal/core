from unittest import TestCase

from manipule_file.ImportData import ImportData
from manipule_file.ManipulateData import ManipulateData
from preprocessamento.PreProcessing import PreProcessing
import os

from processamento.Processing import Processing
from testes.ConfTests import ConfTest


class TestProcessing(TestCase):



    def setUp(self) -> None:
        super().setUpClass()
        self.folder_out = os.path.realpath(ConfTest.FOLDER_OUT)
        self.manipulate_data = ManipulateData()
        folder = os.path.join(self.folder_out, "tokens", "remove_stop_words")
        label = "last.txt"
        file_path = os.path.join(folder, label)
        self.list_tokens = self.manipulate_data.read_tokens(file_path)

        self.processing = Processing(ConfTest.LANGUAGE, 1234)

    def test_processa_text_blog(self):
        for texto in self.lista:
            resultado = self.processing.processa_text_blob(texto)
            print(resultado)

    def test_separate_train_and_test_tokens(self):
        full_list = self.list_tokens
        train, test = self.processing.separate_train_and_test_tokens(full_list, 20)
        print("sd")



    def test_get_word_freq(self):
        sub_lista = self.lista
        frequencia = self.processing.get_word_freq(sub_lista)
        print(frequencia.most_common(10))

    def test_create_features(self):
        full_list = self.list_tokens
        train, test = self.processing.separate_train_and_test_tokens(full_list, 20)
        doc_rep_train = self.processing.create_features(train)
        doc_rep_test = self.processing.create_features(test)
        doc_rep = doc_rep_train + doc_rep_test

    def test_train_naive(self):
        full_list = self.list_tokens
        train, test = self.processing.separate_train_and_test_tokens(full_list, 80)
        doc_rep_train = self.processing.create_features(train)
        doc_rep_test = self.processing.create_features(test)
        classifier = self.processing.train_naive(doc_rep_train, doc_rep_test)



