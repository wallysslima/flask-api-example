import requests
from requests import exceptions
from todo import config


DEFAULT_REQUEST_TIMEOUT = 10


class ConnectionError(Exception):
    pass


def get_todos(max_items=5):
    if config.TODO_API_URL is None:
        raise ValueError("Hey, you need to set the enviroment variable TODO_API_URL")

    try:
        # I know that I'm loading few data into python memory, so it's safe to
        # not stream the data.
        response = requests.get(config.TODO_API_URL, timeout=DEFAULT_REQUEST_TIMEOUT)
    except exceptions.ConnectionError:
        raise ConnectionError()

    todos, items = [], response.json()
    current_item_number = 0
    for item in items:
        if current_item_number == max_items:
            break

        todos.append({"id": item.get("id"), "title": item.get("title")})
        current_item_number += 1

    return todos
