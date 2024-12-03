import os

from pydantic_settings import BaseSettings, SettingsConfigDict

from .exceptions import SettingException


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env', env_file_encoding='utf-8', extra='ignore'
    )

    BASE_DIR: str = os.path.abspath(os.path.dirname(__file__))
    ROOT_DIR: str = os.path.dirname(BASE_DIR)

    INCLUDE_APPS: list[str] = ['app']

    ENVIRONMENT: str | None = os.getenv('ENVIRONMENT')

    DATABASE_URL: str | None = os.getenv('DATABASE_URL')
    DEV_DATABASE_URL: str | None = os.getenv('DEV_DATABASE_URL')

    CORS_ORIGINS: list[str] = [
        'http://localhost:3000',
        'http://localhost:3000/leciel/reservation',
    ]
    CORS_ORIGINS_REGEX: str | None = None
    CORS_HEADERS: list[str]

    # JWT
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 15 * 4  # 60 minutes
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 3  # 1 day

    secret_key: str | None = os.getenv('SECRET_KEY')

    if secret_key:
        SECRET_KEY: str = secret_key
    else:
        raise SettingException

    ALGORITHM: str = 'HS256'


settings = Settings()
