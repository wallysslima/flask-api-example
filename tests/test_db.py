from todo import db


class MockAuth:
    def __init__(self, username, password):
        self.username = username
        self.password = password


def test_get_by_username(create_user):
    username = "John"
    assert db.User.by_username(username=username) is None
    create_user(username=username, password="dewey")
    user = db.User.by_username(username=username)
    assert isinstance(user, db.User)
    assert user.username == username


def test_validated_password(create_user):
    user = create_user(username="John", password="Dewey")
    assert user.check_password(password="Dewey") is True
    assert user.check_password(password="dewey") is False
