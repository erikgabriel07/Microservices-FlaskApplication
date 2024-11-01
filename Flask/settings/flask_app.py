from flask import Flask
from settings.config import Config
from settings.logger import Logger
from settings.token_auth import TokenAuthenticator
from database.sessao import db
from routes.routes import register_routes


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    logger = Logger('flask-logger')
    token_authenticator = TokenAuthenticator()

    with app.app_context():
        db.create_all() # Criar todas as tabelas

    register_routes(app, logger, token_authenticator)

    return app
