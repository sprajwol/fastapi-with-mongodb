from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pymongo.errors import ServerSelectionTimeoutError

from configs.app_configs import app_configs
from routers import auth_routes
from database import connection

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=app_configs.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_routes.router)


@app.on_event("startup")
async def startup_event():
    print("--------------------------------STARTUP_EVENT--------------------------------")
    try:
        connection.client.server_info()
        print("--------------------------------MongoDB Connection Successful--------------------------------")
    except ServerSelectionTimeoutError as sste:
        print("--------------------------------ServerSelectionTimeoutError--------------------------------")
        print(sste)
    except Exception as e:
        print("--------------------------------Exception--------------------------------")
        print(e)


@app.on_event("shutdown")
async def shutdown_event():
    print("--------------------------------SHUTDOWN_EVENT--------------------------------")


@app.get("/", tags=["Root"])
def root():
    return {
        "message": "Welcome to the project!"
    }
