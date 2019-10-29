from flask import Flask, request
from http import HTTPStatus

from validacoes import *
from mongoDB import MongoConnect

app = Flask('__name__')


@app.route('/login', methods=['POST'])
def login():
    data = request.json
    garanta = Validacao()

    #Verifica se o ussername existe
    if not garanta.username_existe(data["username"]):
        return 'username inválido!', HTTPStatus.FORBIDDEN

    #Verifica se a senha é valida
    if garanta.username_password_valido(data):
        return 'Logado!', HTTPStatus.ACCEPTED
    return 'password inválido!', HTTPStatus.FORBIDDEN


@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    data = request.json
    db = MongoConnect()
    db.save(data)
    return 'Feito!', HTTPStatus.CREATED
