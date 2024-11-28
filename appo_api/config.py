import os

from pydantic_settings import BaseSettings, SettingsConfigDict


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

    CORS_ORIGINS: list[str]
    CORS_ORIGINS_REGEX: str | None = None
    CORS_HEADERS: list[str]


settings = Settings()
