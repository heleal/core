import csv
import json

class Learquivo:

    def acessaarquivo(self,caminho):

        listaFrases = []
        #caminho = "../dadosOriginal/treino/IMDb-sample-Copy1.csv"
        with open(caminho, encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile, delimiter=",")
            for i, row in enumerate(reader):
                texto = row["Text"]
                listaFrases.append(texto)
        csvfile.close()
        return listaFrases


    def lerArquivoJson(self,caminho):
        listaFrases = []
        f = open(caminho, encoding="utf-8")
        for i, linha in enumerate(f.readlines()):
            d = json.loads(linha)
            texto = d["Text"]
            listaFrases.append(texto)
        f.close()
        return listaFrases