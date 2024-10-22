import datetime

import allure
import httpx
from jsonschema import validate

from core.contracts import create_user_scheme

base_url = 'https://reqres.in/'
create_user = 'api/users'


@allure.suite('Проверка создания пользователя')
@allure.title('Проверяем создания пользователя с именем и работой')
def test_create_user_with_name_and_job():
    body = {
        "name": "morpheus",
        "job": "leader"
    }

    response = httpx.post(base_url + create_user, json=body)
    with allure.step('Проверяем код ответа'):
        assert response.status_code == 201
    creation_date = response.json()["createdAt"].replace('T', ' ')
    current_date = str(datetime.datetime.now(datetime.UTC))

    validate(response.json(), create_user_scheme)

    with allure.step('Проверяем что Имя в ответе = Имя в запросе'):
        assert response.json()["name"] == body["name"]
    with allure.step('Проверяем что работа в ответе = работа в запросе'):
        assert response.json()["job"] == body["job"]
    with allure.step('Проверяем что время создания = текущему времени'):
        assert creation_date[0:16] == current_date[0:16]


@allure.suite('Проверка создания пользователя')
@allure.title('Проверяем создания пользователя только с работой')
def test_create_user_without_name():
    body = {
        "job": "leader"
    }

    response = httpx.post(base_url + create_user, json=body)

    with allure.step('Проверяем код ответа'):
        assert response.status_code == 201
    creation_date = response.json()["createdAt"].replace('T', ' ')
    current_date = str(datetime.datetime.now(datetime.UTC))

    validate(response.json(), create_user_scheme)

    with allure.step('Проверяем что работа в ответе = работа в запросе'):
        assert response.json()["job"] == body["job"]
    with allure.step('Проверяем что время создания = текущему времени'):
        assert creation_date[0:16] == current_date[0:16]


@allure.suite('Проверка создания пользователя')
@allure.title('Проверяем создания пользователя только с именем')
def test_create_user_without_job():
    body = {
        "name": "morpheus"
    }

    response = httpx.post(base_url + create_user, json=body)

    with allure.step('Проверяем код ответа'):
        assert response.status_code == 201

    creation_date = response.json()["createdAt"].replace('T', ' ')
    current_date = str(datetime.datetime.now(datetime.UTC))

    validate(response.json(), create_user_scheme)

    with allure.step('Проверяем что Имя в ответе = Имя в запросе'):
        assert response.json()["name"] == body["name"]
    with allure.step('Проверяем что время создания = текущему времени'):
        assert creation_date[0:16] == current_date[0:16]
