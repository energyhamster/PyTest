from src.enums.user_enums import Statuses
from src.generators.player_localization import PlayerLocalization


class Player:
    def __init__(self):
        self.result = {}
        self.reset()

    def set_status(self, status=Statuses.ACTIVE.value):
        self.result["account_status"] = status
        return self

    def set_balance(self, balance=0):
        self.result["balance"] = balance
        return self

    def set_avatar(self, avatar="https://google.com/"):
        self.result["avatar"] = avatar

    def reset(self):
        self.set_avatar()
        self.set_balance()
        self.set_status()
        self.result["localize"] = {
            "en_US": PlayerLocalization("en_US").build(),
            "uk_UA": PlayerLocalization("uk_UA").build()
        }
        return self

    def update_inner_generator(self, key, generator):
        self.result[key] = {"en": generator.build()}
        return self


    def build(self):
        return self.result
