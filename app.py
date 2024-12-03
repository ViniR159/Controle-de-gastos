from flask import Flask, request, jsonify
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base


bdg = create_engine("sqlite:///gastos.db")
Session = sessionmaker(bind=bdg)
session = Session()

BaseBanco = declarative_base()

class Gasto(BaseBanco):
    __tablename__ = "Gastos"

    Id = Column("Id", Integer, primary_key=True, autoincrement=True)
    Nome = Column("Nome", String)
    Data = Column("Data", Integer)
    Valor = Column("Valor", Integer)

    def __init__(self, Nome, Data, Valor):
        self.Nome = Nome
        self.Data = Data
        self.Valor = Valor


BaseBanco.metadata.create_all(bind=bdg)

# C de Create CRUD

# gastoteste2 = Gasto(Nome="teste2", Data="00.00.00", Valor="25.5") 
# session.add(gastoteste2)
# session.commit()

# R de Read CRUD

todos_os_gasto = session.query(Gasto).all() #.filter_by(parametro="")  .first()
print(todos_os_gasto[0].Nome)

# U de Update CRUD

usuario2 = todos_os_gasto[1]
usuario2.Nome = "testee"
session.add(usuario2)
session.commit()

# D de Delete CRUD

session.delete(usuario2)
session.commit()


# app = Flask(__name__)

# Gastos = 
#     {
#         "Id": "0000",
#         "Nome": "teste",
#         "Data": "00/00/0000",
#         "Valor": 0.0
#     },
#     {
#         "Id": "0001",
#         "Nome": "teste1",
#         "Data": "00/00/0000",
#         "Valor": 0.0
#     },
#     {
#         "Id": "0002",
#         "Nome": "teste2",
#         "Data": "00/00/0000",
#         "Valor": 4.0
#     },
# ]

# # @app.route("/gastos", methods=["GET"])
# # def obter():
# #     return jsonify(Gastos)

# @app.route("/gastos/<string:Id>", methods=["GET"])
# def filtrar_gastos(Id):
#     for Gasto in Gastos:
#         if Gasto.get("Id") == Id:
#             return jsonify(Gastos)

# @app.route("/gastos/<string:Id>", methods=["PUT"])
# def editar_gastos(Id):
#     gasto_editado = request.get_json()
#     for indice,gasto in enumerate(Gastos):
#         if gasto.get("Id") == Id:
#             Gastos[indice].update(gasto_editado)
#             return jsonify(Gastos[indice])

# @app.route("/gastos", methods=["POST"])
# def adicionar_gastos():
#     novo_gasto = request.get_json()
#     Gastos.append(novo_gasto)

#     return jsonify(Gastos)

# @app.route("/gastos/<string:Id>", methods=["DELETE"])
# def deletar_gastos(Id):
#     gasto_editado = request.get_json()
#     for indice,gasto in enumerate(Gastos):
#         if gasto.get("Id") == Id:
#             del Gastos[indice]

#     return jsonify(Gastos)


# if __name__ == "__main__":
#     app.run(port="5000", host="localhost",debug=True)