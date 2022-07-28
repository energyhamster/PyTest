import pytest

from src.generators.player_localization import PlayerLocalization
from src.enums.user_enums import Statuses


@pytest.mark.parametrize("status", Statuses.list())
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


@pytest.mark.parametrize(
    "localizations, loc", [
        ("fr", "fr_FR"), ("it", "it-IT")
    ]
)
def test_player_localization(get_player_generator, localizations, loc):
    localization = get_player_generator.update_inner_value(
        ["localize", localizations], PlayerLocalization(loc).build()).build()
    print(localization)
