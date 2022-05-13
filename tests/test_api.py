from todo import db
from unittest import mock


MOCK_TODOS = [
    {"id": 1, "title": "test"},
]


def test_get_todos(client, create_user):
    create_user(username="user", password="123")
    logs = db.Log.query.all()
    assert logs == []

    with mock.patch("todo.lib.backend.get_todos", return_value=MOCK_TODOS):
        response = client.get("/api/v1/todos")
        assert response.status_code == 401
        response = client.get("/api/v1/todos", auth=("user", "123"))
        assert response.status_code == 200

    log = db.Log.query.one()
    assert log.response_status_code == 200
    assert log.response_data == str(MOCK_TODOS)
