from pydantic import validator
from pydantic_settings import BaseSettings


class AuthConfigs(BaseSettings):
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    class Config:
        extra = "ignore"
        env_file = "./.env"


auth_configs = AuthConfigs()
