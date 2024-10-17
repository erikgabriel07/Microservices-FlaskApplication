from flask import Flask
from settings.config import Config
from database.sessao import db
from routes.routes import register_routes


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        db.create_all() # Criar todas as tabelas

    register_routes(app)    

    return app
