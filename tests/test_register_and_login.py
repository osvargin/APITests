import json

import allure
import httpx
import pytest
from jsonschema import validate

from core.contracts import login_successful_scheme
from core.contracts import register_and_login_scheme
from core.contracts import register_unsuccessful_scheme

json_file = open("core/new_users_data.json")
users_data = json.load(json_file)
base_url = 'https://reqres.in/'
register_user = 'api/register'
login_user = 'api/login'


@allure.suite('Регистрация тестового пользователя')
@allure.title('Выполняем параметризированный запрос на создание 4 пользователей')
@pytest.mark.parametrize('user_data', users_data)
def test_successful_register(user_data):
    response = httpx.post(base_url + register_user, json=user_data)
    with allure.step('Создаем пользователя'):
        assert response.status_code == 200

    validate(response.json(), register_and_login_scheme)


@allure.suite('Регистрация тестового пользователя')
@allure.title('Выполняем запрос на регистрацию без email')
def test_unsuccessful_register():
    body = {
        "email": "sydney@fife"
    }

    response = httpx.post(base_url + register_user, json=body)
    with allure.step('Статус-код = 400'):
        assert response.status_code == 400

    validate(response.json(), register_unsuccessful_scheme)


@allure.suite('Авторизация тестового пользователя')
@allure.title('Выполняем запрос с валидными данными')
@pytest.mark.parametrize('user_data', users_data)
def test_successful_login(user_data):
    response = httpx.post(base_url + login_user, json=user_data)
    with allure.step('Авторизация пользователя'):
        assert response.status_code == 200

    validate(response.json(), login_successful_scheme)
