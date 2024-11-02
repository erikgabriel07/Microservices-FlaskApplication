from flask import Flask, request, jsonify
from settings.logger import Logger
from settings.jwt_manager import JWTManager
from model.transacao import User
from werkzeug.security import check_password_hash


def register_login_route(app: Flask, logger: Logger):
    @app.route('/login', methods=['POST'])
    @logger.api_logging_handler
    def login():
        data = request.get_json()
        jwt_manager = JWTManager(app.config['SECRET_KEY'])

        if data.get('token'):
            if jwt_manager.decode_jwt_token(data.get('token')):
                return jsonify({'mensagem': 'Cliente ainda possui um token válido!'), 409

        usuario = User.query.filter_by(nome=data['user']).first()

        if not usuario or not check_password_hash(usuario.senha_hash, data['pwd']):
            return jsonify(
                {'auth_status': 'deauthorized', 'mensagem': 'Credenciais inválidas!'}), 406
        
        access_token = jwt_manager.generate_jwt_token(usuario.nome)

        return jsonify({'auth_status': 'authorized', 'access_token': access_token}), 200
