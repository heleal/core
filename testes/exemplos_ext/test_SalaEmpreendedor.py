from unittest import TestCase
import os

from exemplos_ext.SalaEmpreendedor import SalaEmpreendedor


class TestSalaEmpreendedor(TestCase):



    def setUp(self) -> None:
        super().setUp()
        self.path_file_csv = os.path.abspath("D:\\workspace\\analize_sentimentos\\dados\\pt-BR\\base_sala_empreendedor.csv")
        self.sala_empreendedor = SalaEmpreendedor()

    def test_inicializa_dados(self):
        path_file = self.path_file_csv
        dados = self.sala_empreendedor.inicializa_dados(path_file)
        print(dados)

    def test_gera_list_pontos(self):
        lista_pontos = self.sala_empreendedor.gera_list_pontos()
        print(lista_pontos)

    def test_gera_list_irrelevantes(self):
        lista_pontos = self.sala_empreendedor.gera_list_pontos()
        list_irrelevantes = self.sala_empreendedor.gera_list_irrelevantes(lista_pontos)
        print(list_irrelevantes)

    def test_limpa_dados(self):
        path_file = self.path_file_csv
        dados = self.sala_empreendedor.inicializa_dados(path_file)
        lista_pontos = self.sala_empreendedor.gera_list_pontos()
        list_irrelevantes = self.sala_empreendedor.gera_list_irrelevantes(lista_pontos)
        frase_processada = self.sala_empreendedor.limpa_dados(dados,list_irrelevantes)
        print(frase_processada)

    def test_classificacar_texto(self):
        path_file = self.path_file_csv
        dados = self.sala_empreendedor.inicializa_dados(path_file)
        lista_pontos = self.sala_empreendedor.gera_list_pontos()
        list_irrelevantes = self.sala_empreendedor.gera_list_irrelevantes(lista_pontos)
        frase_processada = self.sala_empreendedor.limpa_dados(dados, list_irrelevantes)
        dados["tratamento_1"] = frase_processada
        print(self.sala_empreendedor.classificacar_texto(dados, "tratamento_1", "Instrumento"))

    def test_nuvem_palavras(self):
        path_file = self.path_file_csv
        dados = self.sala_empreendedor.inicializa_dados(path_file)
        lista_pontos = self.sala_empreendedor.gera_list_pontos()
        list_irrelevantes = self.sala_empreendedor.gera_list_irrelevantes(lista_pontos)
        frase_processada = self.sala_empreendedor.limpa_dados(dados, list_irrelevantes)
        dados["tratamento_1"] = frase_processada

        self.sala_empreendedor.nuvem_palavras_graf("","Orientação Técnica Presencial", dados)
        #self.sala_empreendedor.nuvem_palavras_graf("", "Informação Presencial", dados)
        #self.sala_empreendedor.nuvem_palavras_graf("", "Orientação Técnica a Distância", dados)
        #self.sala_empreendedor.nuvem_palavras_graf("", "Consultoria Presencial", dados)
        #self.sala_empreendedor.nuvem_palavras_graf("", "Informação a Distância", dados)

    def test_tokeniza_data_set(self):
        path_file = self.path_file_csv
        dados = self.sala_empreendedor.inicializa_dados(path_file)
        lista_pontos = self.sala_empreendedor.gera_list_pontos()
        list_irrelevantes = self.sala_empreendedor.gera_list_irrelevantes(lista_pontos)
        frase_processada = self.sala_empreendedor.limpa_dados(dados, list_irrelevantes)
        dados["tratamento_1"] = frase_processada

        frequencia = self.sala_empreendedor.tokeniza_data_set(dados)
        print(frequencia.most_common(20))

    def test_cria_data_frame_frequencia(self):
        path_file = self.path_file_csv
        dados = self.sala_empreendedor.inicializa_dados(path_file)
        lista_pontos = self.sala_empreendedor.gera_list_pontos()
        list_irrelevantes = self.sala_empreendedor.gera_list_irrelevantes(lista_pontos)
        frase_processada = self.sala_empreendedor.limpa_dados(dados, list_irrelevantes)
        dados["tratamento_1"] = frase_processada

        frequencia = self.sala_empreendedor.tokeniza_data_set(dados)
        self.sala_empreendedor.cria_data_frame_frequencia(frequencia)

    def test_pareto(self):
        path_file = self.path_file_csv
        dados = self.sala_empreendedor.inicializa_dados(path_file)
        lista_pontos = self.sala_empreendedor.gera_list_pontos()
        list_irrelevantes = self.sala_empreendedor.gera_list_irrelevantes(lista_pontos)
        frase_processada = self.sala_empreendedor.limpa_dados(dados, list_irrelevantes)
        dados["tratamento_1"] = frase_processada
        self.sala_empreendedor.pareto(dados, "tratamento_1", 10)

    def test_acuracia(self):
        path_file = self.path_file_csv
        dados = self.sala_empreendedor.inicializa_dados(path_file)
        lista_pontos = self.sala_empreendedor.gera_list_pontos()
        list_irrelevantes = self.sala_empreendedor.gera_list_irrelevantes(lista_pontos)
        frase_processada = self.sala_empreendedor.limpa_dados(dados, list_irrelevantes)
        dados["tratamento_1"] = frase_processada
        acuracia_tratamento = self.sala_empreendedor.classificacar_texto(dados, "tratamento_1", "Classificacao")
        print(acuracia_tratamento)