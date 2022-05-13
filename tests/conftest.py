import pytest
from todo import create_app

from todo import db


@pytest.fixture
def app():
    app = create_app(
        {
            "TESTING": True,
            "SECRET_KEY": "123",
        }
    )

    yield app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()


@pytest.fixture
def create_user():
    def _create_user(username, password):
        user = db.User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        return user

    yield _create_user
    db.User.query.delete()
    db.session.commit()
