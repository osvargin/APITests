import datetime

import allure
import httpx
from jsonschema import validate

from core.contracts import update_user_scheme

base_url = 'https://reqres.in/'
update_user = 'api/users/2'


@allure.suite('Проверка частичного обновления пользователя')
@allure.title('Проверяем частичного обновления пользователя с именем и работой')
def test_update_user_with_name_and_job():
    body = {
        "name": "morpheus",
        "job": "zion resident"
    }

    response = httpx.patch(base_url + update_user, json=body)
    with allure.step('Проверяем код ответа'):
        assert response.status_code == 200
    updated_date = response.json()["updatedAt"].replace('T', ' ')
    current_date = str(datetime.datetime.now(datetime.UTC))

    validate(response.json(), update_user_scheme)

    with allure.step('Проверяем что Имя в ответе = Имя в запросе'):
        assert response.json()["name"] == body["name"]
    with allure.step('Проверяем что работа в ответе = работа в запросе'):
        assert response.json()["job"] == body["job"]
    with allure.step('Проверяем что время частичного обновления = текущему времени'):
        assert updated_date[0:16] == current_date[0:16]


@allure.suite('Проверка частичного обновления пользователя')
@allure.title('Проверяем частичного обновления пользователя только с работой')
def test_update_user_without_name():
    body = {
        "job": "zion resident"
    }

    response = httpx.patch(base_url + update_user, json=body)

    with allure.step('Проверяем код ответа'):
        assert response.status_code == 200
    creation_date = response.json()["updatedAt"].replace('T', ' ')
    current_date = str(datetime.datetime.now(datetime.UTC))

    validate(response.json(), update_user_scheme)

    with allure.step('Проверяем что работа в ответе = работа в запросе'):
        assert response.json()["job"] == body["job"]
    with allure.step('Проверяем что время частичного обновления = текущему времени'):
        assert creation_date[0:16] == current_date[0:16]


@allure.suite('Проверка частичного обновления пользователя')
@allure.title('Проверяем частичного обновления пользователя только с именем')
def test_update_user_without_job():
    body = {
        "name": "morpheus"
    }

    response = httpx.patch(base_url + update_user, json=body)

    with allure.step('Проверяем код ответа'):
        assert response.status_code == 200

    creation_date = response.json()["updatedAt"].replace('T', ' ')
    current_date = str(datetime.datetime.now(datetime.UTC))

    validate(response.json(), update_user_scheme)

    with allure.step('Проверяем что Имя в ответе = Имя в запросе'):
        assert response.json()["name"] == body["name"]
    with allure.step('Проверяем что время частичного обновления = текущему времени'):
        assert creation_date[0:16] == current_date[0:16]


