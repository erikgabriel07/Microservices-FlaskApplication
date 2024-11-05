from flask import Flask
from flask_cors import CORS
from settings.jwt_manager import jwt_manager
from settings.config import Config
from settings.logger import Logger
from services.thread_processing import ThreadProcessing
from database.sessao import db
from routes.routes import register_routes
from routes.login import register_login_route
from model.transacao import User
from werkzeug.security import generate_password_hash


def create_default_user(): # Cria um usuário padrão
    transacao = User(
        nome='flask',
        senha_hash=generate_password_hash('flask123')
    )
    try:
        db.session.add(transacao)
        if db.session.commit():
            db.session.close()
    except:
        return None
    return None


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app,  resources=r'/*', origins=['http://localhost:8000'])

    db.init_app(app)
    jwt_manager.init_app(app)

    logger = Logger('flask-logger')
    thread_processor = ThreadProcessing(app)

    with app.app_context():
        db.create_all() # Criar todas as tabelasz
        create_default_user() # Cria um usuário padrão para testes

    register_routes(app, logger, thread_processor)
    register_login_route(app, logger)

    return app
