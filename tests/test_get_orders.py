import requests
from data import BASE_URL, ORDERS_LIST

class TestGetOrders:

    def test_get_orders_returns_list(self):
        response = requests.get(BASE_URL + ORDERS_LIST)

        assert response.status_code == 200
        response_json = response.json()
        assert "orders" in response_json
        assert isinstance(response_json["orders"], list)