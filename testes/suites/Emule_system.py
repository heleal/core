import unittest

from testes.importa_arquivo.test_ManipulateData import TestManipulateData
from testes.preprocessamento.test_PreProcessing import TestPreProcessing
from testes.processamento.test_Processing import TestProcessing


def suite_01():
    suite_class = unittest.TestSuite()
    suite_class.addTest(TestManipulateData('test_create_random_corpus_for_csv'))
    suite_class.addTest(TestPreProcessing('test_generate_tokens'))
    suite_class.addTest(TestPreProcessing('test_remove_punctuation_full'))
    suite_class.addTest(TestPreProcessing('test_remove_stop_word_full'))
    suite_class.addTest(TestProcessing('test_train_naive'))
    return suite_class

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite_01())