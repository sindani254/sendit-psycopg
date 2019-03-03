from werkzeug.security import safe_str_cmp
from .UserModels import User

users = [
    User(1, 'manu', 'sindani254@gmail.com', 'Soen@30010010')
]

username_mapping = {u.username: u for u in users}

email_mapping = {u.email: u for u in users}

userId_mapping = {u.id: u for u in users}


def authenticate(username, password):
    user = username_mapping.get(username, None)
    if user and safe_str_cmp(user.password, password):
        return user


def identity(payload):
    user_id = payload['identity']
    return userId_mapping.get(user_id, None)
