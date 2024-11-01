import jwt
from settings.config import Config


class JWTManager:
    def __init__(self) -> None:
        self.secret_key = Config.SECRET_KEY

    def verify_jwt_token(self, token):
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return None
        except jwt.InvalidTokenError:
            return None
        