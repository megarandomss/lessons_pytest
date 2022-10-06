from pydantic import BaseModel, validator

class Post(BaseModel):
    id: int
    title: str
#   name: str = Field(alias = "_name")

    @validator("id")    # валидация заменяется условием id: int = Field(le=2)
    def check_that_id_id_less_than_two(cls, v):
        if v > 2:
            raise ValueError('Id is not less than two')
        else:
            return v



# [{"id": 1, "title": "Post 1", "_name": "Andrey"}