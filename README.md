# Flask API Example

### Setup the application  
> I'm supposing that you are trying to run this on an Unix enviroment. I haven't tested it on Windows, I don't think it works on Windows.

Follow these steps:

* Install an updated [Python](https://www.python.org/) version, 3.8 or higher.
* Create a [virtual enviroment](https://docs.python.org/3/library/venv.html) to run the application.
* Install the requirements.txt with the command: `pip install -r requirements.txt`
* Install the app: `pip install -e .`
* Install [sqlite3](https://www.sqlite.org/index.html).
* You need to set and export the following enviroment variables:

| config                | Required | Example                                    |
|-----------------------|----------|--------------------------------------------|
| TODO_APP_TESTING      | No       | 1                                          |
| TODO_SECRET_KEY       | Yes      | ```fjdsa23&$234asff```                     |
| TODO_DATABASE_ADDRESS | Yes      | ```sqlite:////tmp/test.db```               |
| TODO_API_URL          | Yes      | https://jsonplaceholder.typicode.com/todos |
| TODO_PASSWORD_SALT    | Yes      | ```fdajf32473471734&$#4831482```           |
* Start the Flask app with the command: `flask run`

It will start the application at `localhost:5000`.


### Creating an user

To create the user, you need to run the custom Flask commands that I created.
Example:
```
flask add-user john 1234
```

The command above will create a user with the username `john` and password `1234`.


### Autid

All the requests create logs that contains the `user_id`, if the user is logged, the `raw response data`, and the `reponse status code`.

example:
```
user,response raw,response code
wallysson,{'error': {'reason': 'Internal Server Error'}},500
wallysson,[{'id': 1, 'title': 'delectus aut autem'}],200
```


### Running the application tests
You need to install the tests requirements, before:
```
pip install -r test_requirements.txt
```

To run all the tests:
```
make test
```


### Requesting the api
You should use the username and password to authenticate the request, using basic auth. Using `curl` for example

```
curl -u username:password http://127.0.0.1:5000/api/v1/todos
```
