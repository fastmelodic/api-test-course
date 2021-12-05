import requests
import pytest


url = 'https://petstore.swagger.io/v2/'


def get_pets_by_status(status):

    return requests.get(url + 'pet/findByStatus', params={'status': status})


@pytest.mark.parametrize('status', ["available", "pending", "sold"])
def test_positive(status):

    r = get_pets_by_status(status)

    assert r.status_code == 200
    for item in r.json():
        assert item['status'] == status
