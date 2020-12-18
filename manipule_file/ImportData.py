import csv
import json


class ImportData:

    def read_csv_file(self, path_file):
        list_comments = []
        with open(path_file, encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file, delimiter=",")
            for i, row in enumerate(reader):
                text = row["Text"]

                list_comments.append(text)
        csv_file.close()
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
