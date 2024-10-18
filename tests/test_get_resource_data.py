import httpx
from jsonschema import validate

from core.contracts import resource_data_scheme

base_url = 'https://reqres.in/'
list_resource = 'api/unknown'
single_resource = 'api/unknown/2'
not_found_resource = 'api/unknown/23'


def test_list_resource():
    response = httpx.get(base_url + list_resource)
    assert response.status_code == 200
    data = response.json()["data"]

    for resource in data:
        validate(resource, resource_data_scheme)
        assert len(str(resource["year"])) == 4
        assert resource["year"] - resource["id"] == 1999
        assert resource["color"].startswith('#')


def test_single_resource():
    response = httpx.get(base_url + single_resource)
    assert response.status_code == 200
    data = response.json()["data"]
    assert len(str(data["year"])) == 4
    assert data["year"] - data["id"] == 1999
    assert data["color"].startswith('#')


def test_not_found_resource():
    response = httpx.get(base_url + not_found_resource)
    assert response.status_code == 404
