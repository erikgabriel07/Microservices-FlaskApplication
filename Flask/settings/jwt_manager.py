import jwt
from datetime import datetime, timedelta


class JWTManager:
    def __init__(self, secret_key, expiration_hours=1) -> None:
        self.secret_key = secret_key
        self.expiration_hours = expiration_hours

    def generate_jwt_token(self, user_id='flask'):
        payload = {
            'sub': user_id,
            'iat': datetime.utcnow(),
            'exp': datetime.utcnow() + timedelta(hours=self.expiration_hours)
        }
        token = jwt.encode(payload, self.secret_key, algorithm='HS256')
        return token

    def decode_jwt_token(self, token):
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=['HS256'])
            return payload
        except jwt.ExpiredSignatureError:
            return None
        except jwt.InvalidTokenError:
            return None
