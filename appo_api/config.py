import os
from typing import Tuple

from pydantic_settings import BaseSettings, SettingsConfigDict

from .exceptions import (
    ClientException,
    SettingException,
    client_exception_handler,
)


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env', env_file_encoding='utf-8', extra='ignore'
    )

    BASE_DIR: str = os.path.abspath(os.path.dirname(__file__))
    ROOT_DIR: str = os.path.dirname(BASE_DIR)

    INCLUDE_APPS: list[str] = ['app']

    secret_key: str | None = os.getenv('SECRET_KEY')
    environment: str | None = os.getenv('ENVIRONMENT')
    database_url: str | None = os.getenv('DATABASE_URL')
    dev_database_url: str | None = os.getenv('DEV_DATABASE_URL')

    if secret_key:
        SECRET_KEY: str = secret_key
    else:
        raise SettingException(detail='SECRET_KEY')

    if environment:
        ENVIRONMENT: str = environment
    else:
        raise SettingException(detail='ENVIRONMENT')

    if database_url:
        DATABASE_URL: str = database_url
    else:
        raise SettingException(detail='DATABASE_URL')

    if dev_database_url:
        DEV_DATABASE_URL: str = dev_database_url
    else:
        raise SettingException(detail='DEV_DATABASE_URL')

    # JWT
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 15 * 4  # 60 minutes
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 3  # 1 day
    ALGORITHM: str = 'HS256'

    # cors
    CORS_ORIGINS: list[str] = [
        'http://localhost:3000',
        'http://localhost:3000/leciel/reservation',
    ]
    CORS_ORIGINS_REGEX: str | None = None
    CORS_HEADERS: list[str]

    # exception
    EXCEPTIONS: list[Tuple] = [(ClientException, client_exception_handler)]


settings = Settings()
