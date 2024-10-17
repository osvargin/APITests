import httpx
from jsonschema import validate

from core.contracts import user_data_scheme

base_url = 'https://reqres.in/'
list_users = 'api/users?page=2'
single_user = 'api/users/2'
not_found = '/api/users/23'
email_ends = "@reqres.in"
avatar_ends = "-image.jpg"


def test_list_users():
    url = base_url + list_users
    response = httpx.get(url)
    assert response.status_code == 200
    data = response.json()["data"]

    for user in data:
        validate(user, user_data_scheme)
        assert user["email"].endswith(email_ends)
        assert str(user["id"]) in user["avatar"]
        assert user['avatar'].endswith(str(user['id']) + avatar_ends)


def test_single_user():
    url = base_url + single_user
    response = httpx.get(url)
    assert response.status_code == 200
    data = response.json()["data"]
    assert data["email"].endswith(email_ends)
    assert str(data["id"]) in data["avatar"]
    assert data['avatar'].endswith(str(data['id']) + avatar_ends)


def test_user_not_found():
    url = base_url + not_found
    response = httpx.get(url)
    assert response.status_code == 404
