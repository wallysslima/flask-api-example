import flask
from flask import session
from werkzeug.exceptions import HTTPException
from todo.api import v1
from todo import db
from todo import cli


def error_handler(e):
    user_id = session.get("user_id")
    if isinstance(e, HTTPException):
        response = e.get_response()
        response.content_type = "application/json"
        response_data = {"error": {"reason": e.name}}
        response.data = flask.json.dumps(response_data)
        db.Log.add(user_id, response_data, e.code)
        return response

    response_data = {"error": {"reason": "Internal Server Error"}}
    db.Log.add(user_id, response_data, 500)
    return flask.jsonify(response_data), 500


def create_app(config=None):
    app = flask.Flask(__name__)
    if config:
        app.config.from_mapping(config)
    else:
        app.config.from_pyfile("config.py")

    db.init()
    cli.init(app)
    app.register_blueprint(v1.bp)
    app.register_error_handler(Exception, error_handler)
    app.do_teardown_appcontext(db.teardown)

    return app
