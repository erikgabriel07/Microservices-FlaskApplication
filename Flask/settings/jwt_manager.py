from flask import jsonify
from flask_jwt_extended import JWTManager


jwt_manager = JWTManager()


@jwt_manager.invalid_token_loader
def invalid_token_callback(error):
    return jsonify({'mensagem': 'O token fornecido é inválido!'}), 401


@jwt_manager.expired_token_loader
def expired_token_callback(header, payload):
    return jsonify({'mensagem': 'O token fornecido expirou!'}), 401


@jwt_manager.unauthorized_loader
def missing_token_callback(error):
     return jsonify({'mensagem': 'Nenhum token de acesso foi fornecido!'}), 401