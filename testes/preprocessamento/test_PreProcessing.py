from datetime import datetime
from unittest import TestCase

from manipule_file.ImportData import ImportData
import os

from manipule_file.ManipulateData import ManipulateData
from preprocessamento.PreProcessing import PreProcessing
from testes.ConfTests import ConfTest


class TestPreProcessing(TestCase):

    @classmethod
    def setUpClass(self) -> None:
        super().setUpClass()
        s = ImportData()
        base_folder = os.path.realpath(ConfTest.FOLDER_DATA)
        file = "IMDb-sample_01.csv"
        path_file = os.path.join(base_folder, file)
        lista = s.read_csv_file(path_file)
        self.lista = lista

        self.limit = 100

        language = ConfTest.LANGUAGE

        self.pre_processing = PreProcessing(language)
        self.folder_out = os.path.realpath(ConfTest.FOLDER_OUT)
        self.manipulate_data = ManipulateData()


    def test_generate_tokens(self):
        folder = os.path.join(self.folder_out, "corpus")
        corous_file_base = "last.txt"
        corpus_file_path = os.path.join(folder, corous_file_base)
        corpus = self.manipulate_data.read_corpus(corpus_file_path)

        folder = os.path.join(self.folder_out, "tokens", "initial")
        label_file_base = "tokens"
        str_time = datetime.now().strftime(ConfTest.TIMESTAMP)
        label_file = label_file_base + str_time + ".txt"

        for comments in corpus:
            tokens = self.pre_processing.generate_tokens(comments)
            self.manipulate_data.write_tokens(tokens, folder, label_file)
        self.manipulate_data.copy_last(os.path.join(folder, label_file), folder)

    def test_remove_punctuation_full(self):
        folder = os.path.join(self.folder_out, "tokens", "initial")
        label = "last.txt"
        file_path = os.path.join(folder, label)
        list_tokens = self.manipulate_data.read_tokens(file_path)

        folder = os.path.join(self.folder_out, "tokens", "remove_punctuation")
        str_time = datetime.now().strftime(ConfTest.TIMESTAMP)
        label_file_base = "remove_punctuation"
        label_file_remove_punctuation = label_file_base + str_time + ".txt"

        label_file_base = "punctuation"
        label_file_punctuation = label_file_base + str_time + ".txt"

        for comment in list_tokens:
            clean_comment = self.pre_processing.remove_punctuation_full(comment)
            self.manipulate_data.write_tokens([clean_comment[0],comment[1]], folder, label_file_remove_punctuation)
            self.manipulate_data.write_tokens([clean_comment[1],comment[1]], folder, label_file_punctuation)
        self.manipulate_data.copy_last(os.path.join(folder, label_file_remove_punctuation), folder)

    def test_remove_stop_word_full(self):
        folder = os.path.join(self.folder_out, "tokens", "remove_punctuation")
        label = "last.txt"
        file_path = os.path.join(folder, label)
        list_tokens = self.manipulate_data.read_tokens(file_path)

        folder = os.path.join(self.folder_out, "tokens", "remove_stop_words")
        str_time = datetime.now().strftime(ConfTest.TIMESTAMP)
        label_file_base = "remove_stop_words"
        label_file_remove_stop_words = label_file_base + str_time + ".txt"

        label_file_base = "stop_words"
        label_file_stop_words = label_file_base + str_time + ".txt"

        for comment in list_tokens:
            clean_comment = self.pre_processing.remove_stop_words_full(comment)
            self.manipulate_data.write_tokens([clean_comment[0], comment[1]],  folder, label_file_remove_stop_words)
            self.manipulate_data.write_tokens([clean_comment[1], comment[1]],  folder, label_file_stop_words)
        self.manipulate_data.copy_last(os.path.join(folder, label_file_remove_stop_words), folder)


