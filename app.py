from flask import Flask, request, jsonify
from peewee import *

db = SqLiteDatabase("Gastos.db")

class Id(Model):
    nome = CharField()
    data = CharField()
    valor = CharField()

    class Meta:
        database = db

class

app = Flask(__name__)

Gastos = [
    {
        "Id": "0000",
        "Nome": "teste",
        "Data": "00/00/0000",
        "Valor": 0.0
    },
    {
        "Id": "0001",
        "Nome": "teste1",
        "Data": "00/00/0000",
        "Valor": 0.0
    },
    {
        "Id": "0002",
        "Nome": "teste2",
        "Data": "00/00/0000",
        "Valor": 4.0
    },
]

@app.route("/gastos", methods=["GET"])
def obter():
    return jsonify(Gastos)

@app.route("/gastos/<string:Id>", methods=["GET"])
def filtrar_gastos(Id):
    for Gasto in Gastos:
        if Gasto.get("Id") == Id:
            return jsonify(Gastos)

@app.route("/gastos/<string:Id>", methods=["PUT"])
def editar_gastos(Id):
    gasto_editado = request.get_json()
    for indice,gasto in enumerate(Gastos):
        if gasto.get("Id") == Id:
            Gastos[indice].update(gasto_editado)
            return jsonify(Gastos[indice])

@app.route("/gastos", methods=["POST"])
def adicionar_gastos():
    novo_gasto = request.get_json()
    Gastos.append(novo_gasto)

    return jsonify(Gastos)

@app.route("/gastos/<string:Id>", methods=["DELETE"])
def deletar_gastos(Id):
    gasto_editado = request.get_json()
    for indice,gasto in enumerate(Gastos):
        if gasto.get("Id") == Id:
            del Gastos[indice]

    return jsonify(Gastos)


if __name__ == "__main__":
    app.run(port="5000", host="localhost",debug=True)