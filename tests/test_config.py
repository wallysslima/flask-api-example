import os
import pytest

from todo import config


def test_get_config_required_variable_not_on_enviroment():
    with pytest.raises(ValueError) as exception:
        config.get("qualquer_variavel", required=True)
    assert "Hey, a required config variable is not on environment" in str(
        exception.value
    )


def test_get_config_using_converter():
    key = "TODOXXXXX"
    os.environ[key] = "1"
    assert config.get(key, converter=None) == "1"
    assert config.get(key, converter=bool) == True
    os.environ.pop(key, None)
