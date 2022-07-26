import pytest

from src.base_classes.response import Response
from src.schemas.user import User


@pytest.mark.production
def test_getting_users_list(get_users, calculate, make_number):
    """
    In this test we validate user JSON schema
    """
    Response(get_users).assert_status_code(200).validate(User)
    print(calculate(1, 1))
    print(make_number)


@pytest.mark.skip('[ISSUE-23233] Issue with network connection')
def test_another():
    """
    In this test we try to check that 1 is equal to 1
    """
    assert 1 == 1


def test_another_fail():
    """
    In this test we try to check that 1 is equal to 2
    """
    assert 1 == 2


@pytest.mark.development
@pytest.mark.parametrize("first_value, second_value, result", [
    (1, 2, 3),
    (-1, -2, -3),
    (-1, 2, 1),
    ("a", 2, None),
    ("a", "b", None)
])
def test_calculator(first_value, second_value, result, calculate):
    """
    In test we are testing calculating with different values(Valid and not valid)
    """
    assert calculate(first_value, second_value) == result
