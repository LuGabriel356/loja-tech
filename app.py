from flask import Flask, render_template, url_for

app = Flask(__name__)



@app.route("/")
def inicio():
    return render_template("login.html")


@app.route("/usuarios/listar")
def listar_usuarios():
    return render_template("usuarios/usuarios.html")


@app.route("/usuarios/inserir")
def inserir_usuario():
    return render_template("usuarios/usuarios-form.html")


@app.route("/pecas/listar")
def listar_pecas():
    return render_template("pecas/pecas.html")


@app.route("/pecas/inserir")
def inserir_peca():
    return render_template("pecas/pecas-form.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")










if __name__ == "__main__":
    app.run(debug=True)
