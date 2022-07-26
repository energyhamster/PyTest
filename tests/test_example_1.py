import requests
from configuration import SERVICE_URL
from src.base_classes.response import Response
from src.schemas.user import User


def test_getting_users_list():
    response = requests.get(SERVICE_URL)
    test_object = Response(response)
    test_object.assert_status_code(2030).validate(User)
