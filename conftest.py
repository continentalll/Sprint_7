import pytest
import requests
from data import BASE_URL, COURIER_LOGIN, COURIER_DELETE
from courier_helpers import register_new_courier_and_return_login_password


@pytest.fixture
def new_courier():

    login_pass = register_new_courier_and_return_login_password()
    assert login_pass, "Не удалось создать курьера в фикстуре"

    courier = {
        "login": login_pass[0],
        "password": login_pass[1],
        "firstName": login_pass[2],
    }

    login_response = requests.post(BASE_URL + COURIER_LOGIN, json={
        "login": courier["login"],
        "password": courier["password"]
    })
    courier_id = login_response.json().get("id")

    yield courier

    if courier_id:
        requests.delete(BASE_URL + COURIER_DELETE.format(courier_id))