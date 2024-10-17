from flask import request, jsonify
from database.sessao import db
from models.transacao import Transacao


def register_routes(app):
    @app.route('/transacao', methods=['POST'])
    def criar_transacao():
        data = request.get_json()

        nova_transacao = Transacao(
            conta=data['conta'],
            agencia=data['agencia'],
            texto=data.get('texto', None),
            valor=data['valor'],
        )

        db.session.add(nova_transacao)
        db.session.commit()

        return jsonify({'mensagem': 'Transação realizada com sucesso!'}), 200
    