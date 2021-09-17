from functools import wraps
from flask import request
#import config
#from app.db import session, Usert
#import jwt

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        SECRET_KEY = '123447a47f563e90fe2db0f56b1b17be62378e31b7cfd3adc776c59ca4c75e2fc512c15f69bb38307d11d5d17a41a7936789'
        SECRET_USER = '2gbnhf5'
        token = None
        user = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
            user = request.headers['x-access-user']
        if not token or not user:
            return 'Acceso no autorizado 1!', 401
        if token != SECRET_KEY or user != SECRET_USER :
            return 'Acceso no autorizado 2!', 401

        #records = session.query(Usert).filter(Usert.usuario == 'YO')      
        #try:
        #    current_user = db.find_one({'usario': user})
        #    if not current_user:
        #        return 'Acceso no autorizado 2!', 401
        #except:
        #    return 'Acceso no autorizado 3!', 401
        
        return f(*args, **kwargs)

    return decorated

'''
CREATE TABLE usuarios (id INTEGER PRIMARY KEY AUTOINCREMENT,usuario TEXT NOT NULL,key TEXT NOT NULL);
INSERT INTO usuarios (usuario, key) VALUES ('2gbnhf5', '123447a47f563e90fe2db0f56b1b17be62378e31b7cfd3adc776c59ca4c75e2fc512c15f69bb38307d11d5d17a41a7936789');
'''
