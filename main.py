from flask import Flask, request, render_template, redirect
import sqlite3

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def tabela_site():
    bancodedados = sqlite3.connect("gastos.db")
    cursor = bancodedados.cursor()

    if request.method == "POST":
        nome_de_gasto = request.form["Nome_do_gasto"]
        Data = request.form["Data"]
        Valor = request.form["Valor"]

        cursor.execute("INSERT INTO Gastos (nome, Data, Valor) VALUES (?, ?, ?)", (nome_de_gasto, Data, Valor))
        bancodedados.commit()
        print(bancodedados)

        return redirect('/')

    cursor.execute('SELECT * FROM Gastos')
    data = cursor.fetchall()
    headers = [description[0] for description in cursor.description]

    bancodedados.close()

    return render_template("index.html", headers=headers, data=data)


@app.route("/delete", methods=["POST"])
def delete_row():
    row_id = request.form["ID"]

    bancodedados = sqlite3.connect("gastos.db")
    cursor = bancodedados.cursor()
    cursor.execute("DELETE FROM Gastos WHERE ID = ?", (row_id,))
    bancodedados.commit()
    bancodedados.close()

    return redirect("/")



if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)   
