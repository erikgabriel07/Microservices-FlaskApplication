from flask import request, jsonify
from database.sessao import db
from model.transacao import Transacao


def register_routes(app):
    @app.route('/cadastrar/transacao', methods=['POST'])

    def criar_transacao():
        try:
            data = request.get_json()
            nova_transacao = Transacao(
                conta=data.get('conta'),
                agencia=data['agencia'],
                texto=data.get('texto', None),
                valor=data['valor']    
            )
            db.session.add(nova_transacao)
            db.session.commit()
            return jsonify({'mensagem': 'Transacao realizada'}), 200
        except Exception as e:
            return jsonify({'mensagem': f'Erro{e}'}), 500

    @app.route('/listar/transacao', methods=['GET'])
    def listar_transacao():
        transacoes = Transacao.query.all()
        resultados = []
        resultados_deletados = []
        for transacao in transacoes:
            if transacao.is_deleted or transacao.is_duplicated:
                result = {
                    'id': transacao.id,
                    'conta': transacao.conta,
                    'agencia': transacao.agencia,
                    'texto': transacao.texto,
                    'valor': transacao.valor,
                    'deletada': transacao.is_deleted,
                    'duplicada': transacao.is_duplicated
                }
                resultados_deletados.append(result)
            else:
                result = {
                    'id': transacao.id,
                    'conta': transacao.conta,
                    'agencia': transacao.agencia,
                    'texto': transacao.texto,
                    'valor': transacao.valor
                }
                resultados.append(result)
        return jsonify({'Dados Deletados ou Duplicados: ': resultados_deletados, 'Dados ativos: ':resultados}), 200
    
    @app.route('/excluir/<int:id>', methods=['DELETE'])
    def delete(id):
        transacao = Transacao.query.get(id)
        if transacao is None:
            pass
        transacao.is_deleted = True
        db.session.commit()
        return jsonify({'mensagem':'deletado'}), 200
    
    @app.route('/duplicado/<int:id>', methods=['PATCH'])
    def duplicado(id):
        transacao = Transacao.query.get(id)
        if transacao is None:
            pass
        transacao.is_duplicated = True
        db.session.commit()
        return jsonify({'mensagem':'deletado'}), 200