from pydantic import BaseModel
from pydantic.types import List
from src.schemas.physical import Physical
from src.schemas.owners import Owners


class DetailedInfo(BaseModel):
    physical: Physical
    owners: List[Owners]
