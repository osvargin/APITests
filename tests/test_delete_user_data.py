import datetime

import allure
import httpx
from jsonschema import validate

base_url = 'https://reqres.in/'
delete_user = 'api/users/2'


@allure.suite('Проверка удаления пользователя')
@allure.title('Проверяем удаления пользователя с именем и работой')
def test_update_user_with_name_and_job():

    response = httpx.delete(base_url + delete_user)
    with allure.step('Проверяем код ответа'):
        assert response.status_code == 204