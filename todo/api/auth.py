from todo import db
from functools import wraps
from flask import request
from flask import session


def login_required(f):
    @wraps(f)
    def wrapped_view(**kwargs):
        auth = request.authorization
        not_authorized = (
            "Unauthorized",
            401,
            {"WWW-Authenticate": 'Basic realm="Login Required"'},
        )
        if not auth:
            return not_authorized

        user = db.User.by_username(auth.username)
        if not user:
            return not_authorized

        if not user.check_password(auth.password):
            return not_authorized

        session["user_id"] = user.id
        return f(**kwargs)

    return wrapped_view
