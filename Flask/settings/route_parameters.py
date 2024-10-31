from functools import wraps
from flask import jsonify


def verify_id_parameter(f):
    
    @wraps(f)
    async def decorator(*args, **kwargs):
        id = kwargs.get('id') # Recupera o ID passado para a rota

        if not id:
            # Se nenhum ID for fornecido, lança uma exceção
            return jsonify({'message': 'Nenhum ID fornecido!'}), 400
        return await f(*args, **kwargs)
    
    return decorator
