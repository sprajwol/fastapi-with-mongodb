from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from configs.app_configs import app_configs

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=app_configs.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["Root"])
def root():
    return {
        "message": "Welcome to the project!"
    }
