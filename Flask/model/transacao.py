from werkzeug.security import generate_password_hash, check_password_hash
from database.sessao import db


class BaseIncidencia(db.Model):
    __tablename__ = 'base_de_incidencia'

    id = db.Column(db.Integer, primary_key=True)
    ano_calendario = db.Column(db.Integer, nullable=False)
    receita_tributaria = db.Column(db.Integer, nullable=False)
    descricao = db.Column(db.String(180), nullable=True)
    valor_receita_tributaria = db.Column(db.Numeric(15,2), nullable=False)
    percentual_pib = db.Column(db.Numeric(3,2), nullable=False)
    is_deleted = db.Column(db.Boolean, default=False)
    is_duplicated = db.Column(db.Boolean, default=False)


class TributoCompetencia(db.Model):
    __tablename__ = 'tributo_e_competencia'

    id = db.Column(db.Integer, primary_key=True)
    ano_calendario = db.Column(db.Integer, nullable=False)
    competencia = db.Column(db.String(180), nullable=False)
    orcamento = db.Column(db.String(180), nullable=False)
    descricao = db.Column(db.String(180), nullable=False)
    valor_receita_tributaria = db.Column(db.Numeric(15,2), nullable=False)
    percentual_pib = db.Column(db.Numeric(3,2), nullable=False)
    is_deleted = db.Column(db.Boolean, default=False)
    is_duplicated = db.Column(db.Boolean, default=False)


# Tabela usada apenas para testes de geração de token utilizando dados
# preexistentes no banco
class User(db.Model): 
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), unique=True, nullable=False)
    senha_hash = db.Column(db.String(255), nullable=False)

    def definir_senha(self, senha):
        self.senha_hash = generate_password_hash(senha)

    def checar_senha(self, senha):
        return check_password_hash(self.senha_hash, senha)