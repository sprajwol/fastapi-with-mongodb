from pydantic import validator
from pydantic_settings import BaseSettings


class AppConfigs(BaseSettings):
    APP_ENV: str = "local"
    ALLOWED_ORIGINS: str

    class Config:
        extra = "ignore"
        env_file = "./.env"

    @validator('ALLOWED_ORIGINS')
    def allowed_origin_convert_to_list(cls, value):
        print(value)
        return value.split(',')


app_configs = AppConfigs()
