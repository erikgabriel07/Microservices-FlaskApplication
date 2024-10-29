from database.sessao import db


class Transacao(db.Model):
    __tablename__ = 'transacao'
    id = db.Column(db.Integer, primary_key=True)
    conta = db.Column(db.String(20), nullable=False)
    agencia = db.Column(db.String(10), nullable=False)
    texto = db.Column(db.String(), nullable=True)
    valor = db.Column(db.Float(), nullable=False)
    is_deleted = db.Column(db.Boolean,nullable=False, default=False)
    is_duplicated = db.Column(db.Boolean, default=False)
    