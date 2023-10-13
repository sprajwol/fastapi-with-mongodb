from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from schemas import schemas

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)


@router.post('/signup')
async def signup(user: schemas.User):
    return "signup"


@router.post('/login', response_model=schemas.Token)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
):
    return form_data
