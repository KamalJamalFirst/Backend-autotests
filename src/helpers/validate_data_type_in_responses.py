from pydantic import BaseModel, PydanticTypeError

class PostNewUserDataTypeValidator(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    username: str


    def parse_data(self, response):
        try:
            self.parse_obj(response)
        except PydanticTypeError as e:
            print(e)