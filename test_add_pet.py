import requests
from random import randint, choice
import string


url = 'https://petstore.swagger.io/v2/'


def post_pet(data):

    return requests.post(url + 'pet', json=data)


def delete_pet(pet_id):

    return requests.delete(url + f'pet/{pet_id}')


def test_positive():

    id = randint(0, 10000)
    category_name = ''.join(choice(string.ascii_lowercase) for i in range(10))
    name = ''.join(choice(string.ascii_lowercase) for i in range(6))
    url = 'http://www.' + ''.join(choice(string.ascii_lowercase) for i in range(6)) + '.com'
    tag = ''.join(choice(string.ascii_lowercase) for i in range(4))
    status = 'available'

    data = {
        'id': id,
        'category': {
            'name': category_name
        },
        'name': name,
        'photoUrls': [
            url
        ],
        'tags': [
            {
                'name': tag
            }
        ],
        'status': status
    }

    create_pet = post_pet(data)

    delete_pet(create_pet.json()['id'])

    assert create_pet.status_code == 200
    assert create_pet.json()['name'] == name
