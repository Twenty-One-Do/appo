from enum import Enum


class TokenType(str, Enum):
    ACCESS: str = 'access'
    REFRESH: str = 'refresh'


class Gender(str, Enum):
    MALE = 'MALE'
    FEMALE = 'FEMALE'
