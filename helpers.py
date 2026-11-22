import random
import string


def generate_random_string(length=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def generate_courier_payload():
    return {
        "login": generate_random_string(),
        "password": generate_random_string(),
        "firstName": generate_random_string()
    }


def generate_order_payload(color=None):
    payload = {
        "firstName": "Тест",
        "lastName": "Тестов",
        "address": "Пермь, ул. Тестовая, 1",
        "metroStation": 4,
        "phone": "+79999999999",
        "rentTime": 5,
        "deliveryDate": "2025-01-01",
        "comment": "Тестовый заказ",
    }
    if color is not None:
        payload["color"] = color
    return payload