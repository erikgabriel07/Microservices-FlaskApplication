import logging, os
import logging.handlers
from functools import wraps
from flask import request


class Logger(logging.Logger):
    def __init__(self, name: str, level=logging.INFO) -> None:
        super().__init__(name, level)
        os.makedirs(os.path.join('logs'), exist_ok=True)

        file_handler = logging.handlers.RotatingFileHandler(
            filename=os.path.join('Flask', 'logs', 'app.log'),
            maxBytes=1000000,
            backupCount=3
        )
        file_handler.formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        self.addHandler(file_handler)

    def context_log(self, level, message, context_message):
        if context_message:
            message = f'{message} | {context_message}'

        return self.log(level, message)
    
    def api_logging_handler(self, f):
        @wraps(f)
        def decorator(*args, **kwargs):
            message = f'{request.remote_addr} - /{request.method} {request.full_path}'

            context = f'{request.user_agent}'
            
            self.context_log(logging.INFO, message, context)

            return f(*args, *kwargs)
        
        return decorator
