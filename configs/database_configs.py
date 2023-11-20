from pydantic import validator
from pydantic_settings import BaseSettings


class DatabaseConfigs(BaseSettings):
    MONGODB_CONNECTION_STRING: str
    DB_NAME: str
    USERS_COLLECTION: str

    class Config:
        extra = "ignore"
        env_file = "./.env"


database_configs = DatabaseConfigs()
