from database.sessao import db


class base_incidencia(db.Model):
    __tablename__ = 'base_de_incidencia'

    id = db.Column(db.Integer, primary_key=True)
    ano_calendario = db.Column(db.Integer, nullable=False)
    receita_tributaria = db.Column(db.Integer, nullable=False)
    descricao = db.Column(db.String(), nullable=True)
    valor_receita_tributaria = db.Column(db.Numeric(15,2), nullable=False)
    percentual_pib = db.Column(db.Numeric(3,2), nullable=False)
    is_deleted = db.Column(db.Boolean, default=False)
    is_duplicated = db.Column(db.Boolean, default=False)


class tributo_competencia(db.Model):
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
