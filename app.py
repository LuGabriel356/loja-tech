from flask import Flask, render_template

app = Flask(__name__)



@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/usuarios")
def usuarios():
    return render_template("usuarios.html")


@app.route("/usuarios/cadastrar")
def cadastrar_usuario():
    return render_template("cadastrar_usuario.html")


@app.route("/pecas")
def pecas():
    return render_template("pecas.html")


@app.route("/pecas/cadastrar")
def cadastrar_peca():
    return render_template("cadastrar_peca.html")


@app.route("/vendas")
def vendas():
    return render_template("vendas.html")


@app.route("/vendas/cadastrar")
def cadastrar_venda():
    return render_template("cadastrar_venda.html")










if __name__ == "__main__":
    app.run(debug=True)
