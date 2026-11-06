import os

from dotenv import load_dotenv
from flask import Flask, redirect, render_template, request, url_for
from flask_wtf.csrf import CSRFProtect

from db import execute_one

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

# Liga a proteção CSRF: todo formulário POST do sistema vai precisar do token
CSRFProtect(app)


# ==============================================================================
# PÁGINAS PRINCIPAIS
# ==============================================================================

@app.route("/")
def inicio():
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

# ==============================================================================
# USUÁRIOS
# ==============================================================================

@app.route("/usuarios/listar")
def listar_usuarios():
    return render_template("usuarios/usuarios.html")


@app.route("/usuarios/inserir")
def inserir_usuario():
    return render_template("usuarios/usuarios-form.html")

# ==============================================================================
# PRODUTOS
# ==============================================================================

@app.route("/produtos/listar")
def listar_produtos():
    return render_template("produtos/produtos.html")


@app.route("/produtos/inserir", methods=['GET', 'POST'])
def inserir_produto():

    if request.method== 'POST':
        redirect(url_for(listar_perfis))

    return render_template("produtos/produtos-form.html")

# ==============================================================================
# PERFIS
# ==============================================================================

@app.route("/perfis/inserir")
def inserir_perfil():
    return render_template("perfis/perfil-form.html")

@app.route("/perfis/listar")
def listar_perfis():
    return render_template("perfis/perfis-listar.html")





























# ==============================================================================
# TELAS DE ERROS
# ==============================================================================

@app.errorhandler(404)
def pagina_nao_encontrada(erro):
    return render_template('404.html'), 404


@app.errorhandler(500)
def erro_no_servidor(erro):
    return render_template('500.html'), 500

if __name__ == "__main__":
    app.run(debug=True)