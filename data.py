BASE_URL = "https://qa-scooter.education-services.ru"

COURIER_CREATE = "/api/v1/courier"
COURIER_LOGIN = "/api/v1/courier/login"
COURIER_DELETE = "/api/v1/courier/{}"
ORDERS_CREATE = "/api/v1/orders"
ORDERS_LIST = "/api/v1/orders"

ERROR_MESSAGES = {
    "courier_exists": "Этот логин уже используется. Попробуйте другой.",
    "missing_field": "Недостаточно данных для создания учетной записи",
    "login_failed": "Учетная запись не найдена",
    "missing_login": "Недостаточно данных для входа"
}