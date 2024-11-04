from flask import Flask, request, jsonify
from flask_jwt_extended import (
    create_access_token, create_refresh_token,
    verify_jwt_in_request, get_jwt_identity, jwt_required
)
from flask_jwt_extended.exceptions import NoAuthorizationError
from settings.logger import Logger
from model.transacao import User
from werkzeug.security import check_password_hash


def register_login_route(app: Flask, logger: Logger):
    @app.route('/login', methods=['POST'])
    @logger.api_logging_handler
    @jwt_required(optional=True)
    def login():
        data = request.get_json()

        try:
            verify_jwt_in_request()

            identity = get_jwt_identity()
            return jsonify({'mensagem': f'Usuário {identity} já está logado!'}), 409
        except NoAuthorizationError as e:
            pass

        usuario = User.query.filter_by(nome=data.get('user')).first()

        if not usuario or not check_password_hash(usuario.senha_hash, data.get('pwd')):
            return jsonify({'mensagem': 'Credenciais inválidas!'}), 406
        
        
        access_token = create_access_token(usuario.id)
        refresh_token = create_refresh_token(usuario.id)

        return jsonify({'access_token': access_token, 'refresh_token': refresh_token}), 200

    @app.route('/refresh/token', methods=['POST'])
    @logger.api_logging_handler
    @jwt_required(refresh=True)
    def refresh_token():
        identity = get_jwt_identity()
        new_access_token = create_access_token(identity)

        return jsonify({'access_token': new_access_token}), 200