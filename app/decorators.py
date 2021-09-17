from flask import request
import config
from app.db import db
from functools import wraps
import jwt


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return 'Acceso no autorizado!', 401
        try:
            coll = db[config.MONGO_AUTH]
            data = jwt.decode(token, config.SECRET_KEY)
            current_user = coll.find_one({'user_id': data['user_id']})
            if not current_user:
                return 'Acceso no autorizado!', 401
        except:
            return 'Acceso no autorizado!', 401
        return f(*args, **kwargs)

    return decorated