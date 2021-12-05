import requests
import pytest
from random import randint, choice
import string


url = 'https://petstore.swagger.io/v2/'


def get_user(username):

    return requests.get(url + f'user/{username}')


def put_user(username, data):

    return requests.put(url + f'user/{username}', json=data)


def create_user(data):

    return requests.post(url + f'user', json=data)


def rand_string():

    return ''.join(choice(string.ascii_lowercase) for i in range(10))


@pytest.mark.parametrize('username',  ['wrong', 'error'])
def test_negative(username):

    r = get_user(username)

    assert r.status_code == 404
    assert r.json()['type'] == 'error'
    assert r.json()['message'] == 'User not found'


def test_put_user():

    username = 'test1'#rand_string()
    data = {
          "id": randint(0, 10000),
          "username": username,
          "firstName": rand_string(),
          "lastName": rand_string(),
          "email": rand_string(),
          "password": rand_string(),
          "phone": rand_string(),
    }

    create_user(data)
    user = get_user(username).json()
    user['phone'] = 'newTestValue'
    put_user(username, user)
    updated_user = get_user(username)

    assert updated_user.json()['phone'] == 'newTestValue'
