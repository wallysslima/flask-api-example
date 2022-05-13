import os


def get(variable_name, required=False, converter=None):
    value = os.environ.get(variable_name)
    if required and not value:
        raise ValueError(
            f"Hey, a required config variable is not on environment. Please "
            f"set and export {variable_name}."
        )
    if converter:
        return converter(value)
    return value


TESTING = get("TODO_APP_TESTING", converter=bool)
SECRET_KEY = get("TODO_SECRET_KEY", required=True)

TODO_DATABASE_ADDRESS = get("TODO_DATABASE_ADDRESS", required=True)
TODO_API_URL = get("TODO_API_URL", required=True)
TODO_PASSWORD_SALT = get("TODO_PASSWORD_SALT", required=True)
