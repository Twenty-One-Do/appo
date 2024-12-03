from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from appo_api.config import settings

DATABASE_URL = (
    settings.DATABASE_URL
    if settings.ENVIRONMENT == 'PROD'
    else settings.DEV_DATABASE_URL
)

engine = create_engine(DATABASE_URL+"?charset=utf8")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
