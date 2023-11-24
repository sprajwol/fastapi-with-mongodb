from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from passlib.context import CryptContext

from database import connection
from schemas import schemas

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@router.post('/signup')
async def signup(user: schemas.User):
    try:
        user = dict(user)
        user['password'] = get_password_hash(user['password'])

        users_collection = connection.users_collection
        filter = {
            "$or": [
                {"username": user['username']},
                {"email": user['email']}
            ]
        }
        users = get_multiple(users_collection, filter)
        if list(users):
            raise ValueError(
                "User with given username and/or email already exists.")

        user = users_collection.insert_one(user)

    except ValueError as e:
        print('ValueError')
        print(e)
        return JSONResponse(
            content=str(e),
            status_code=status.HTTP_406_NOT_ACCEPTABLE
        )

    except Exception as e:
        print('Exception')
        print(e)
        return JSONResponse(
            content=str(e),
            status_code=status.HTTP_400_BAD_REQUEST
        )
    
    body = {"detail": "User has been created successfully."}

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=body
    )


@router.post('/login', response_model=schemas.Token)
async def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
):
    print(f"form_data ==> {form_data}")
    users_collection = connection.users_collection
    user = authenticate_user(
        users_collection, form_data.username, form_data.password)

    return {
        "access_token": "yes",
        "token_type": "Bearer"
    }


def authenticate_user(users_collection, username, password):
    filter = {"username": username}
    user = get_one(users_collection, filter)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Invalid Credentials")

    verified = verify_password(password, user['password'])
    if not verified:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Invalid Credentials")


def verify_password(input_password, saved_hashed_password):
    return pwd_context.verify(input_password, saved_hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def get_one(collection, filter: dict, projection: dict = {}):
    return collection.find_one(filter, projection)


def get_multiple(collection, filter: dict, projection: dict = {}):
    return collection.find(filter, projection)
