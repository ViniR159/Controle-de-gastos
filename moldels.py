from main import *
from sqlalchemy import create_engine, Column, String, Integer, jsonify
from sqlalchemy.orm import sessionmaker, declarative_base

bdg = create_engine("sqlite:///gastos.db")
Session = sessionmaker(bind=bdg)
session = Session()

BaseBanco = declarative_base()

class Gasto(BaseBanco):
    __tablename__ = "Gastos"

    Id = Column("Id", Integer, primary_key=True, autoincrement=True)
    Nome = Column("Nome", String)
    Data = Column("Data", String)
    Valor = Column("Valor", Integer)

    def __init__(self, Nome, Data, Valor):
        self.Nome = Nome
        self.Data = Data
        self.Valor = Valor


BaseBanco.metadata.create_all(bind=bdg)

@app.route("/Gasto", methods=["GET"])
def listar_gastos():
    gastos = session.query(Gasto).all()
    return jsonify([{"id": g.Id, "nome": g.Nome, "data": g.Data, "valor": g.Valor} for g in gastos])


@app.route("/Gasto", methods=["POST"])
def adicionar_gasto():
    dados = request.get_json()
    novo_gasto = Gasto(Nome=dados["Nome"], Data=dados["Data"], Valor=dados["Valor"])
    session.add(novo_gasto)
    session.commit()

def ver():
    todos_os_gasto = session.query(Gasto).all() #.filter_by(parametro="")  .first()
    return todos_os_gasto

# C de Create CRUD

gastoteste = Gasto(Nome="aaaaa", Data="00.00.00", Valor="125.5") 
session.add(gastoteste)
session.commit()

# R de Read CRUD

todos_os_gasto = session.query(Gasto).all() #.filter_by(parametro="")  .first()
print(todos_os_gasto)

# U de Update CRUD

# usuario2 = todos_os_gasto[0]
# usuario2.Nome = "testee"
# session.add(usuario2)
# session.commit()

# D de Delete CRUD

# session.delete(usuario2)
# session.commit()
