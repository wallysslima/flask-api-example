import flask
from werkzeug.exceptions import UnprocessableEntity
from todo.lib import backend
from todo import db
from todo.api import auth


bp = flask.Blueprint("v1", __name__, url_prefix="/api/v1")


def success(data, status_code=200):
    user_id = flask.session.get("user_id")
    db.Log.add(user_id, str(data), status_code)
    return flask.jsonify(data), status_code


@bp.route("/todos")
@auth.login_required
def todos():
    try:
        return success(backend.get_todos())
    except backend.ConnectionError:
        raise UnprocessableEntity()
