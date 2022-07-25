from pydantic import BaseModel, validator


class Post(BaseModel):
    id: int
    title: str

    @validator("id")
    def check_that_id_is_less_than_two(cls, value):
        if value > 2:
            raise ValueError("Id is not less than two")
        else:
            return value
