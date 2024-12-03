from datetime import datetime, timedelta, timezone
from functools import lru_cache

import jwt
from passlib.context import CryptContext

from appo_api.config import settings

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


@lru_cache
def verify_password(plain_password: str, hashed_password: str) -> bool:
    result: bool = pwd_context.verify(plain_password, hashed_password)
    return result


def get_password_hash(password: str) -> str:
    hashed_password: str = pwd_context.hash(password)
    return hashed_password

def create_jwt(data: dict, expires: int | None) -> bytes:
    to_encode = data.copy()
    if expires is not None:
        expire = datetime.now(timezone.utc) + timedelta(minutes=expires)
        to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(
        to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM
    )
    return encoded_jwt
