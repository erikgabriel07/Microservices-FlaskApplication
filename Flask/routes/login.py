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


        usuario = User.query.filter_by(nome=data.get('user')).first()

        if not usuario or not check_password_hash(usuario.senha_hash, data['pwd']):
            return jsonify(
                {'auth_status': 'deauthorized', 'mensagem': 'Credenciais inválidas!'}), 406
        
        if data.get('token'):
            if jwt_manager.decode_jwt_token(data.get('token')):
                return jsonify({'mensagem': 'Cliente ainda possui um token válido!'}), 409
            else:
                return jsonify({'mensagem': 'Token expirou! Faça login novamente!',
                                'access_token': None}), 200
        
        access_token = jwt_manager.generate_jwt_token(usuario.nome)

        return jsonify({'auth_status': 'authorized', 'access_token': access_token}), 200
