import pytest
import requests
from data import BASE_URL, COURIER_LOGIN, ERROR_MESSAGES
from helpers import generate_random_string

class TestLoginCourier:

    def test_login_success(self, new_courier):
        response = requests.post(BASE_URL + COURIER_LOGIN, json={
            "login": new_courier["login"],
            "password": new_courier["password"]
        })

        assert response.status_code == 200
        assert "id" in response.json()
        assert isinstance(response.json()["id"], int)

    @pytest.mark.parametrize("field", ["login", "password"])
    def test_login_missing_field_error(self, new_courier, field):
        payload = {
            "login": new_courier["login"],
            "password": new_courier["password"]
        }
        payload.pop(field)

        response = requests.post(BASE_URL + COURIER_LOGIN, json=payload)

        assert response.status_code == 400
        assert ERROR_MESSAGES["missing_login"] in response.text

    def test_login_wrong_password_error(self, new_courier):
        response = requests.post(BASE_URL + COURIER_LOGIN, json={
            "login": new_courier["login"],
            "password": generate_random_string()
        })

        assert response.status_code == 404
        assert ERROR_MESSAGES["login_failed"] in response.text

    def test_login_nonexistent_user_error(self):
        response = requests.post(BASE_URL + COURIER_LOGIN, json={
            "login": generate_random_string(),
            "password": generate_random_string()
        })

        assert response.status_code == 404
        assert ERROR_MESSAGES["login_failed"] in response.text