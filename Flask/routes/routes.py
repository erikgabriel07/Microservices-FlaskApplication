from flask import Flask, request, jsonify
from flask_jwt_extended import jwt_required
from flask_caching import Cache
from settings.logger import Logger
from model.transacao import BaseIncidencia, TributoCompetencia, TaskResult
from database.sessao import db
from services.thread_processing import ThreadProcessing
import ast


def register_routes(app: Flask, logger: Logger, thread_processor: ThreadProcessing):
    @app.route('/task/status', methods=['GET'])
    @logger.api_logging_handler
    @jwt_required()
    def task_status():
        task_id = request.args.get('id')

        task = TaskResult.query.filter_by(task_id=task_id).first()

        if not task:
            return jsonify({'mensagem': 'Tarefa não encontrada!'}), 404
        
        if task.status == 'processing':
            return jsonify({'mensagem': 'A tarefa ainda está sendo processada!'}), 202
        elif task.status == 'processed':
            data = ast.literal_eval(task.result)
            return data, 200

    @app.route('/file/list-data', methods=['GET'])
    @logger.api_logging_handler
    @jwt_required()
    @thread_processor.thread_processing
    def list_file_data(request_data, request_args, user_id=None):
        data = request_data
        page = int(request_args.get('page', 1))
        per_page = int(request_args.get('per_page', 100))

        if data.get('bi'):
            transacoes = BaseIncidencia.query.filter_by(is_deleted=False).paginate(
                page=page, per_page=per_page, error_out=False
            )
            resultados = [transacao.to_dict() for transacao in transacoes]
            
        elif data.get('tc'):
            transacoes = TributoCompetencia.query.filter_by(is_deleted=False).paginate(
                page=page, per_page=per_page, error_out=False
            )
            resultados = [transacao.to_dict() for transacao in transacoes]

        return jsonify({'data': resultados}), 200

    @app.route('/upload-file/base-incidencia', methods=['POST'])
    @logger.api_logging_handler
    @jwt_required()
    @thread_processor.thread_processing
    def base_incidencia_upload(request_data, request_args, user_id=None):
        try:
            data = request_data

            for data in data:
                transacao = BaseIncidencia(
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
    @jwt_required()
    @thread_processor.thread_processing
    def tributo_competencia_upload(request_data, request_args, user_id=None):
        try:
            data = request_data

            for data in data:
                transacao = TributoCompetencia(
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
    @jwt_required()
    def delete(id, user_id=None):
        return jsonify({'message': 'Deleted successfully!'}), 200
