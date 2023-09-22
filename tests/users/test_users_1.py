import pytest

values = [
    ("C2210", 1, 2, 3),
    ("C2211", -1, -2, -3),
    ("C2212", -1, 2, 1),
    ("C2213", "a", 2, None),
    ("C2214", "a", "b", None)
]


@pytest.fixture(params=values)
def value(request):
    return request.param


def test_calculator(record_property, value, calculate):
    record_property("test_id", value[0])
    result_of_calculation = calculate(value[1], value[2])

    assert result_of_calculation == value[3]
