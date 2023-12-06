from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

class Connection:
    def __init__(self, colecao):
        self.uri = "----------"
        self.client = MongoClient(self.uri, server_api=ServerApi('1'))
        self.banco = self.client['AC4']
        self.x = colecao
        self.colecao = self.banco[colecao]  # Cadastro, Exercicios

        try:
            self.client.admin.command('ping')
            print('Conexão feita com MongoDB')
        except Exception as e:
            print(e)

    def fechar_conexao(self):
        self.client.close()




