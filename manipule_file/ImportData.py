import csv
import json
import os
import random


class ImportData:

    def read_csv_file(self, path_file):
        list_comments = []
        with open(path_file, encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file, delimiter=",")
            for i, row in enumerate(reader):
                text = row["Text"]
                sentiment = row['Sentiment']
                list_comments.append([text,sentiment])
        csv_file.close()
        return list_comments

    def read_folder_csv(self, path_folder, limit, sentiment, is_random=False):
        list_comments = []
        all_files = os.listdir(path_folder)
        if (is_random == True):
            random.shuffle(all_files)
        sub_list = all_files[:limit]
        for label_file in sub_list:
            path_file = os.path.join(path_folder, label_file)
            with open(path_file, 'r', newline='', encoding="utf-8") as comment:
                comment_a = {}
                comment_a["text"] = ""
                for line in comment:
                    comment_a["text"] += line
                comment_a["sentiment"] = sentiment
            list_comments.append(comment_a)
        return list_comments

    def read_json(self, path_file):
        list_comments = []
        f = open(path_file, encoding="utf-8")
        for i, line in enumerate(f.readlines()):
            d = json.loads(line)
            text = d["Text"]
            list_comments.append(text)
        f.close()
        return list_comments
