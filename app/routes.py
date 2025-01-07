from flask import render_template, Flask

from . import create_app  # Importa a função create_app

app = create_app()  # Chama a função para criar a instância de app


@app.route('/')
def index():
    return render_template('index.html')