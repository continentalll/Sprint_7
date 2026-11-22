import pytest
import requests
from data import BASE_URL, COURIER_CREATE, COURIER_LOGIN, ERROR_MESSAGES
from helpers import generate_courier_payload, generate_random_string

class TestCreateCourier:

    def test_create_courier_success(self):
        payload = generate_courier_payload()
        response = requests.post(BASE_URL + COURIER_CREATE, json=payload)

        assert response.status_code == 201
        assert response.json() == {"ok": True}

        login_resp = requests.post(BASE_URL + COURIER_LOGIN, json={
            "login": payload["login"],
            "password": payload["password"]
        })
        courier_id = login_resp.json().get("id")
        if courier_id:
            requests.delete(f"{BASE_URL}/api/v1/courier/{courier_id}")

    def test_create_duplicate_courier_error(self, new_courier):
        response = requests.post(BASE_URL + COURIER_CREATE, json=new_courier)

        assert response.status_code == 409
        assert ERROR_MESSAGES["courier_exists"] in response.text

    @pytest.mark.parametrize("field", ["login", "password"])
    def test_create_courier_missing_field_error(self, field):
        payload = generate_courier_payload()
        payload.pop(field)

        response = requests.post(BASE_URL + COURIER_CREATE, json=payload)

        assert response.status_code == 400
        assert ERROR_MESSAGES["missing_field"] in response.text

    def test_create_courier_existing_login_error(self):
        first_payload = generate_courier_payload()
        requests.post(BASE_URL + COURIER_CREATE, json=first_payload)

        second_payload = {
            "login": first_payload["login"],
            "password": generate_random_string(),
            "firstName": generate_random_string()
        }
        response = requests.post(BASE_URL + COURIER_CREATE, json=second_payload)

        assert response.status_code == 409
        assert ERROR_MESSAGES["courier_exists"] in response.text

        login_resp = requests.post(BASE_URL + COURIER_LOGIN, json={
            "login": first_payload["login"],
            "password": first_payload["password"]
        })
        courier_id = login_resp.json().get("id")
        if courier_id:
            requests.delete(f"{BASE_URL}/api/v1/courier/{courier_id}")