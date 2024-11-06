from flask import jsonify, request
from functools import wraps
from threading import Thread
from model.transacao import TaskResult
from database.sessao import db
import uuid


class ThreadProcessing:
    def __init__(self, app) -> None:
        self.app = app

    def thread_processing(self, f):
        """
        Decorador para executar as operações de uma rota em segundo plano.
        Útil para quando uma enorme quantidade de dados está sendo processado,
        evitando bloquear o endpoint até a tarefa ser totalmente concluída.
        :param f: A função a ser decorada
        :return: A função decoradora
        """
        @wraps(f)
        def decorator(*args, **kwargs):
            task_id = str(uuid.uuid4())

            try:
                result = TaskResult(task_id=task_id, status='processing')
                db.session.add(result)
                if db.session.commit():
                    db.session.close()
            except Exception as e:
                return str(e)

            request_data = request.json
            request_args = request.args
            def target():
                with self.app.app_context():
                    result = f(request_data, request_args, *args, **kwargs)

                    task = TaskResult.query.filter_by(task_id=task_id).first()
                    task.status = 'processed'
                    task.result = str(result[0].get_json())
                    
                    if db.session.commit():
                        db.session.close()


            thread = Thread(target=target)
            thread.start()

            return jsonify({
                'mensagem': 'Requisição está sendo processada em segundo plano. ' \
                    'Acesse a rota de verificação de tarefa para ver seu status.',
                'id_tarefa': task_id
            }), 202
        
        return decorator