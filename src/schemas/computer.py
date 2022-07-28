from pydantic import BaseModel
from pydantic.types import PastDate, FutureDate
from pydantic.networks import IPv4Address, IPv6Network
from src.schemas.detailed_info import DetailedInfo

from computer_example import computer

from src.enums.user_enums import Statuses


class Computer(BaseModel):
    id: int
    status: Statuses
    activated_at: PastDate
    expiration_at: FutureDate
    host_v4: IPv4Address
    host_v6: IPv6Network
    detailed_info: DetailedInfo


comp = Computer.parse_obj(computer)

print(comp.schema_json())
