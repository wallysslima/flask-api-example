from todo import create_app


def test_app_factory():
    assert create_app({"TESTING": False}).testing is False
    assert create_app({"TESTING": True}).testing is True


def test_custom_error_handler(client):
    response = client.get("/api/v1/qualquer_coisa")
    assert response.status_code == 404
    assert response.json == {"error": {"reason": "Not Found"}}
