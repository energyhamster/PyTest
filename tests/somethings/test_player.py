import pytest

from src.generators.player_localization import PlayerLocalization


@pytest.mark.parametrize("status", [
    "ACTIVE",
    "BANNED",
    "DELETED",
    "INACTIVE"
])
def test_player_status(status, get_player_generator):
    print(get_player_generator.set_status(status).build())

@pytest.mark.parametrize("balance_value", [
    "0",
    "1",
    "100",
    "101"
])
def test_player_balance(balance_value, get_player_generator):
    print(get_player_generator.set_balance(balance_value).build())

def test_player_localization(get_player_generator):
    localization = get_player_generator.update_inner_generator("localize", PlayerLocalization("fr_FR")).build()
    print(localization)
