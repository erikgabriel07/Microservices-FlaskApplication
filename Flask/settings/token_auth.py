from functools import wraps
from settings.jwt_manager import JWTManager
from flask import request, jsonify


class TokenAuthenticator:
    def __init__(self, secret_key) -> None:
        self.secret_key = secret_key

    def validate_token(self, f):
        @wraps(f)
        def decorator(*args, **kwargs):
            token = None
            if 'Authorization' in request.headers:
                token = request.headers['Authorization'].split(' ')[1]

            if not token:
                return jsonify({'mensagem': 'Token ausente!'}), 403
            
            try:
                user_id = JWTManager(self.secret_key).decode_jwt_token(token)
                if not user_id:
                    return jsonify({'mensagem': 'Token inválido!'}), 403
            except:
                return jsonify({'mensagem': 'Token inválido!'}), 403

            return f(user_id=user_id, *args, **kwargs)
        
        return decorator