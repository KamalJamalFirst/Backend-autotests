from pydantic import BaseModel, PydanticTypeError
from loguru import logger

class PostNewUserDataTypeValidator(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    username: str
@logger.catch()
def parse_data(response):
    try:
        PostNewUserDataTypeValidator.parse_obj(response)
    except PydanticTypeError as e:
        return e
    return True