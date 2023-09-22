import pytest


# from src.base_classes.response import Response
# from src.schemas.user import User
# from src.schemas.computer import Computer
# from computer_example import computer


# @pytest.mark.production
# def test_getting_users_list(get_users, calculate, make_number):
#     """
#     In this test we validate user JSON schema
#     """
#     Response(get_users).assert_status_code(200).validate(User)
#     print(calculate(1, 1))
#     print(make_number)


# @pytest.mark.skip('[ISSUE-23233] Issue with network connection')
# def test_another():
#     """
#     In this test we try to check that 1 is equal to 1
#     """
#     assert 1 == 1
#
#
# def test_another_fail():
#     """
#     In this test we try to check that 1 is equal to 2
#     """
#     assert 1 == 2


@pytest.mark.development
@pytest.mark.parametrize("test_rail_case_id, first_value, second_value, result", [
    ("C2210", 1, 2, 3),
    ("C2211", -1, -2, -3),
    ("C2212", -1, 2, 1),
    ("C2213", "a", 2, None),
    ("C2214", "a", "b", None)
])
def test_calculator(test_rail_case_id, first_value, second_value, result, calculate, record_property):
    record_property("test_id", test_rail_case_id)
    assert calculate(first_value, second_value) == result

# def test_pydantic_obj():
#     comp = Computer.parse_obj(computer)
#     print(comp.detailed_info.owners)
