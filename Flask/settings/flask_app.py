from flask import Flask
from settings.config import Config
from settings.logger import Logger
from settings.token_auth import TokenAuthenticator
from database.sessao import db
from routes.routes import register_routes
from model.transacao import User


def create_default_user():
    transacao = User(
        nome='flask',
        senha=User().definir_senha('flask123')
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

    db.init_app(app)

    logger = Logger('flask-logger')
    token_authenticator = TokenAuthenticator(app.config['SECRET_KEY'])

    with app.app_context():
        db.create_all() # Criar todas as tabelas
        create_default_user() # Cria um usuário padrão para testes

    register_routes(app, logger, token_authenticator)

    return app
