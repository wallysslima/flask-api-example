from flask.cli import with_appcontext
import click
from todo import db


@click.command("list-users")
@with_appcontext
def list_users():
    users = db.User.query.all()
    for user in users:
        print(user.username)


@click.command("add-user")
@click.argument("username")
@click.argument("password")
@with_appcontext
def add_user(username, password):
    user = db.User(username, password)
    db.session.add(user)
    db.session.commit()


@click.command("audit")
@with_appcontext
def audit():
    logs = db.Log.query.all()
    print("user,response raw,response code")
    for log in logs:
        username = log.user and log.user.username or "-"
        print(f"{username},{log.response_data},{log.response_status_code}")


def init(app):
    commands = [
        add_user,
        audit,
        list_users,
    ]

    for command in commands:
        app.cli.add_command(command)
