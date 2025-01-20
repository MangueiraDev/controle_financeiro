from flask import render_template

# Definir rota
def init_routes(app):
    @app.route('/')
    def index():
        return render_template('index.html')