from flask import Flask, request, render_template, redirect
import sqlite3

app = Flask(__name__)

@app.route('/', methods=["GET", "POST", "DELETE"])
def tabela_site():
    bancodedados = sqlite3.connect("gastos.db")
    cursor = bancodedados.cursor()

    if request.method == "POST ":
        nome_de_gasto = request.form["Nome_do_gasto"]
        Data = request.form["Data"]
        Valor = request.form["Valor"]

        cursor.execute("INSERT INTO Gastos (nome, Data, Valor) VALUES (?, ?, ?)", (nome_de_gasto, Data, Valor))
        bancodedados.commit()

        return redirect('/')

    cursor.execute('SELECT * FROM Gastos')
    data = cursor.fetchall()
    headers = [description[0] for description in cursor.description]

    bancodedados.close()

    return render_template("index.html", headers=headers, data=data)




if __name__ == "__main__":
    app.run(debug=True)