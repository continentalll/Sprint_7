import pytest
import requests
from data import BASE_URL, ORDERS_CREATE
from helpers import generate_order_payload

class TestCreateOrder:

    @pytest.mark.parametrize("color", [
        ["BLACK"],
        ["GREY"],
        ["BLACK", "GREY"],
        None
    ], ids=["black", "grey", "black_and_grey", "no_color"])
    def test_create_order_with_colors(self, color):
        payload = generate_order_payload(color=color)
        response = requests.post(BASE_URL + ORDERS_CREATE, json=payload)

        assert response.status_code == 201
        assert "track" in response.json()
        assert isinstance(response.json()["track"], int)