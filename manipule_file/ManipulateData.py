import os
import re
import shutil
import json
import csv
import random
from itertools import count


class ManipulateData:

    def write_tokens(self, comments_tokens, folder, label):
        label_file = os.path.join(folder, label)
        with open(label_file, 'a', newline='', encoding="utf-8") as csvfile:
            csv_writer = csv.writer(
                csvfile, delimiter=';',
                quotechar='|', quoting=csv.QUOTE_MINIMAL
            )
            a = [comments_tokens[1]] + comments_tokens[0]
            csv_writer.writerows([a])

    def copy_file(self, orig, dst):
        shutil.copyfile(orig, dst, follow_symlinks=True)

    def copy_last(self, orig, folder):
        dst = os.path.join(folder, "last.txt")
        self.copy_file(orig, dst)

    def read_tokens(self, path_file):
        label_file = path_file
        with open(label_file, 'r', newline='', encoding="utf-8") as csvfile:
            csv_reader = csv.reader(
                csvfile, delimiter=';',
                quotechar='|', quoting=csv.QUOTE_MINIMAL
            )
            list_tokens = []
            for row in csv_reader:
                sent = row[0]
                text = row[1:]
                list_tokens.append([text, sent])
            return list_tokens

    def write_corpus(self, corpus, folder, label):
        label_file = os.path.join(folder, label)
        with open(label_file, 'a', newline='', encoding="utf-8") as csv_file:
            csv_writer = csv.writer(
                csv_file, delimiter=';',
                quotechar='|', quoting=csv.QUOTE_MINIMAL
            )
            for comment in corpus:
                row = [comment["text"], comment["sentiment"]]
                csv_writer.writerow(row)

    def read_corpus(self, path_file):
        label_file = path_file
        with open(label_file, 'r', newline='', encoding="utf-8") as csvfile:
            csv_reader = csv.reader(
                csvfile, delimiter=';',
                quotechar='|', quoting=csv.QUOTE_MINIMAL
            )
            corpus = []
            for row in csv_reader:
                corpus.append(row)
            return corpus

    def write_freq_dist(self, path_file, freq, num):
        with open(path_file, 'a', newline='', encoding="utf-8") as csv_file:
            csv_writer = csv.writer(
                csv_file, delimiter=';',
                quotechar='|', quoting=csv.QUOTE_MINIMAL
            )
            for key, count in freq.most_common(num):
                csv_writer.writerow([key, count])

    def create_random_corpus(self, list_comments: list, limit):
        random_list = list_comments.copy()
        random.shuffle(random_list)
        sub_list_random = random_list[:limit]
        return sub_list_random