import json

import allure
import httpx
import pytest
from jsonschema import validate
from core.contracts import register_and_login_scheme

json_file = open("core/new_users_data.json")
users_data = json.load(json_file)
base_url = 'https://reqres.in/'
register_user = 'api/login'

@allure.suite('Регистрация тестового пользователя')
@allure.title('Выполняем параметризированный запрос на создание 4 пользователей')
@pytest.mark.parametrize('user_data', users_data)
def test_successful_register(user_data):
    response = httpx.post(base_url + register_user, json=user_data)
    with allure.step('Создаем пользователя'):
        assert response.status_code == 200

    validate(response.json(), register_and_login_scheme)

