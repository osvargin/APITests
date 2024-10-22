import allure
import httpx
from jsonschema import validate

from core.contracts import resource_data_scheme

base_url = 'https://reqres.in/'
list_resource = 'api/unknown'
single_resource = 'api/unknown/2'
not_found_resource = 'api/unknown/23'


@allure.suite('Проверка запросов списка ресурсов')
@allure.title('Проверяем получение списка ресурсов')
def test_list_resource():
    with allure.step(f'Делаем запрос по адресу: {base_url + list_resource}'):
        response = httpx.get(base_url + list_resource)
    with allure.step('Проверяем статус-код ответа'):
        assert response.status_code == 200

    data = response.json()["data"]

    for resource in data:
        with allure.step('Проверяем элемент из списка'):
            validate(resource, resource_data_scheme)
    with allure.step('Проверяем что длина года равна 4 символам'):
        assert len(str(resource["year"])) == 4
    with allure.step('Проверяем что разница между годом и id = 1999'):
        assert resource["year"] - resource["id"] == 1999
    with allure.step('Проверяем что значение цвета начинается с #'):
        assert resource["color"].startswith('#')


@allure.suite('Проверка запроса одного ресурса')
@allure.title('Проверяем получение одного ресурса по id')
def test_single_resource():
    with allure.step(f'Проверяем запрос по адресу: {base_url + single_resource}'):
        response = httpx.get(base_url + single_resource)
    with allure.step('Проверяем статус-код ответа'):
        assert response.status_code == 200

    data = response.json()["data"]

    with allure.step('Проверяем что длина года равна 4 символам'):
        assert len(str(data["year"])) == 4
    with allure.step('Проверяем что разница между годом и id = 1999'):
        assert data["year"] - data["id"] == 1999
    with allure.step('Проверяем что значение цвета начинается с #'):
        assert data["color"].startswith('#')


@allure.suite('Проверка запроса несуществующего ресурса')
@allure.title('Проверяем получение ресурса по несуществующему id')
def test_not_found_resource():
    with allure.step(f'Проверяем запрос по адресу: {base_url + not_found_resource}'):
        response = httpx.get(base_url + not_found_resource)
    with allure.step('Проверяем статус-код ответа'):
        assert response.status_code == 404
