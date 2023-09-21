import pytest

# from src.generators.player_localization import PlayerLocalization
# from src.enums.user_enums import Statuses


# @pytest.mark.skip()
# @pytest.mark.parametrize("status", Statuses.list())
# def test_player_status(status, get_player_generator):
#     print(get_player_generator.set_status(status).build())


@pytest.mark.parametrize("test_rail_case_id, balance_value", [
    ("C2190", "0"),
    ("C2191", "1"),
    ("C2192", "100"),
    ("C2193", "101")
])
def test_player_balance(test_rail_case_id, balance_value, get_player_generator, record_property):
    record_property("test_id", f"{test_rail_case_id}")
    print(get_player_generator.set_balance(balance_value).build())

# @pytest.mark.skip()
# @pytest.mark.parametrize(
#     "localizations, loc", [
#         ("fr", "fr_FR"), ("it", "it-IT")
#     ]
# )
# def test_player_localization(get_player_generator, localizations, loc):
#     localization = get_player_generator.update_inner_value(
#         ["localize", localizations], PlayerLocalization(loc).build()).build()
#     print(localization)
