from typing import Annotated, Union

from pydantic import BaseModel, EmailStr


class User(BaseModel):
    first_name: str
    last_name: str
    username: str
    email: EmailStr


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Union[str, None] = None
