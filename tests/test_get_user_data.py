import allure
import httpx
from jsonschema import validate

from core.contracts import user_data_scheme

base_url = 'https://reqres.in/'
list_users = 'api/users?page=2'
single_user = 'api/users/2'
not_found = '/api/users/23'
email_ends = "@reqres.in"
avatar_ends = "-image.jpg"


@allure.suite('Проверка запросов данных пользователей')
@allure.title('Проверяем получение списка пользователей')
def test_list_users():
    with allure.step(f'Делаем запрос по адресу {base_url + list_users}'):
        url = base_url + list_users
    response = httpx.get(url)
    with allure.step('Проверяем код ответа'):
        assert response.status_code == 200
    data = response.json()["data"]

    for user in data:
        with allure.step('Проверяем элемент из списка'):
            validate(user, user_data_scheme)
            with allure.step('Проверяем окончание Email адреса'):
                assert user["email"].endswith(email_ends)
            with allure.step('Проверяем наличие id в ссылке на аватарку'):
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
