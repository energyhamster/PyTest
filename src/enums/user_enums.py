from enum import Enum
from src.base_classes.py_enum import PyEnum


class Genders(Enum):
    FEMALE = "female"
    MALE = "male"


class Statuses(PyEnum):
    INACTIVE = "inactive"
    ACTIVE = "active"


class UserErrors(Enum):
    WRONG_EMAIL = "Email doesn't contain @"
