from pprint import pprint
from pymongo import MongoClient

class MongoConnect():

    def __init__(self):
        self.cliente = MongoClient('localhost', 27017)
        self.banco = self.cliente.login  # nome do banco
        self.aluno = self.banco.usuarios  # nome da coleção

    def save(self, json):
        try:
            self.aluno.insert_one(json)
        except Exception as e:
            print("problema ao SALVAR registro")
            print(json)
            print(e)

    def read(self, query=None, projection=None):
        for pessoa in self.aluno.find(query, projection):
            return pessoa

    def find_one(self, query=None, projection=None):
        for pessoa in self.aluno.find(query, projection):
            return True


    def update(self, json, fields):
        try:
            self.aluno.update(json, fields)
        except Exception as e:
            print("problema ao UPDATE registro")
            print(json)
            print(e)


    def delete(self, json):
        try:
            self.aluno.remove(json)
        except Exception as e:
            print("problema ao DELETAR registro")
            print(json)
            print(e)