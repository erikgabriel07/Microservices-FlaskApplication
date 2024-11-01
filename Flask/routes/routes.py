from flask import Flask, request, jsonify
from settings.logger import Logger
from model.transacao import base_incidencia, tributo_competencia
from database.sessao import db


def register_routes(app: Flask, logger: Logger, token_authenticator):
    @app.route('/file/list-data', methods=['GET'])
    @logger.api_logging_handler
    @token_authenticator.validate_token
    def list_file_data(user_id=None):
        data = request.get_json()

        if data.get('bi'):
            transacoes = base_incidencia.query.filter_by(is_deleted=False)

            resultados = [
                {
                    'id': transacao.id,
                    'ano_calendario': transacao.ano_calendario,
                    'receita_tributaria': transacao.receita_tributaria,
                    'descricao': transacao.descricao,
                    'valor_receita_tributaria': transacao.valor_receita_tributaria,
                    'percentual_pib': transacao.percentual_pib,
                    'is_duplicated': transacao.is_duplicated
                } for transacao in transacoes
            ]
            
        elif data.get('tc'):
            transacoes = tributo_competencia.query.filter_by(is_deleted=False)

            resultados = [
                {
                    'id': transacao.id,
                    'ano_calendario': transacao.ano_calendario,
                    'competencia': transacao.competencia,
                    'orcamento': transacao.orcamento,
                    'descricao': transacao.descricao,
                    'valor_receita_tributaria': transacao.valor_receita_tributaria,
                    'percentual_pib': transacao.percentual_pib,
                    'is_duplicated': transacao.is_duplicated
                    
                } for transacao in transacoes
            ]

        return jsonify({'data': resultados}), 200

    @app.route('/upload-file/base-incidencia', methods=['POST'])
    @logger.api_logging_handler
    @token_authenticator.validate_token
    def base_incidencia_upload(user_id=None):
        try:
            data = request.get_json()

            for data in data:
                transacao = base_incidencia(
                    ano_calendario=data.get('Ano_calendario'),
                    receita_tributaria=data.get('Codigo_da_Receita_Tributaria'),
                    descricao=data.get('Descricao'),
                    valor_receita_tributaria=data.get('Valor_da_Receita_Tributaria'),
                    percentual_pib=data.get('Percentual_do_PIB'),
                    is_deleted=False,
                    is_duplicated=False
                )
                db.session.add(transacao)
            if db.session.commit():
                db.session.close()
            
            return jsonify({'mensagem': 'Transação realizada com sucesso!'}), 200
        except Exception as e:
            return jsonify({'mensagem': 'Erro ao cadastrar transação!',
                            'error': e}), 400

    @app.route('/upload-file/tributo-competencia', methods=['POST'])
    @logger.api_logging_handler
    @token_authenticator.validate_token
    def tributo_competencia_upload(user_id=None):
        try:
            data = request.get_json()

            for data in data:
                transacao = tributo_competencia(
                    ano_calendario=data.get('Ano_calendario'),
                    competencia=data.get('Competencia'),
                    orcamento=data.get('Orcamento'),
                    descricao=data.get('Descricao'),
                    valor_receita_tributaria=data.get('Valor_da_Receita_Tributaria'),
                    percentual_pib=data.get('Percentual_do_PIB'),
                    is_deleted=False,
                    is_duplicated=False
                )
                db.session.add(transacao)
            if db.session.commit():
                db.session.close()
            
            return jsonify({'mensagem': 'Transação realizada com sucesso!'}), 200
        except Exception as e:
            return jsonify({'mensagem': 'Erro ao cadastrar transação!',
                            'error': e}), 400

    @app.route('/file/delete/?id=<int:id>', methods=['PATCH'])
    @logger.api_logging_handler
    @token_authenticator.validate_token
    def delete(id, user_id=None):
        return jsonify({'message': 'Deleted successfully!'}), 200
