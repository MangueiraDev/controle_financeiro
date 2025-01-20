from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect

# Inicialização de extensões
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
csrf = CSRFProtect()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    # Inicialização de extensões com o app
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    csrf.init_app(app)

    # Definir a página de login
    login_manager.login_view = 'login'  # Substitua 'login' pela sua rota de login
    login_manager.login_message = "Por favor, faça login para acessar esta página."

    # Importar rotas e registrar
    with app.app_context():
        from .routes import init_routes
        from .models import User  # Certifique-se de que o modelo User está implementado no models.py

        # Registrar as rotas
        init_routes(app)

        # Definir o user_loader
        @login_manager.user_loader
        def load_user(user_id):
            return User.query.get(int(user_id))  # Substitua conforme o modelo do usuário

    return app