from datetime import timedelta

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///transacoes.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = 'KwNTYbvqGdpviK9RCiPgmHLoD1tAHfqyoADwmLZI7mE'

    JWT_ALGORITHM = 'HS256'
    JWT_DECODE_ALGORITHM = ['HS256']
    JWT_ERROR_MESSAGE_KEY = 'mensagem'
    JWT_COOKIE_SAMESITE = 'lax'
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=10)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(hours=1)