test: export TODO_DATABASE_ADDRESS = sqlite://
test: export TODO_API_URL = https://mock.mock
test: export TODO_PASSWORD_SALT = i132
test: export TODO_SECRET_KEY = i132

shell: export TODO_DATABASE_ADDRESS = sqlite://
shell: export TODO_API_URL = https://mock.mock
shell: export TODO_PASSWORD_SALT = i132

test:
	pytest


shell:
	ipython
