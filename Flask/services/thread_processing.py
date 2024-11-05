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
            def target(request_data, task_id):
                with self.app.app_context():
                    result = f(request_data=request_data, *args, **kwargs)

                    task = TaskResult.query.filter_by(task_id=task_id).first()
                    task.status = 'processed'
                    task.result = str(result[0].get_json())
                    
                    if db.session.commit():
                        db.session.close()


            thread = Thread(target=target, args=(request_data, task_id))
            thread.start()

            return jsonify({
                'mensagem': 'Requisição está sendo processada em segundo plano. ' \
                    'Acesse a rota de verificação de tarefa para ver seu status.',
                'id_tarefa': task_id
            }), 202
        
        return decorator