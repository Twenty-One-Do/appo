import re

from fastapi import Form, Header
from pydantic import validator

from ...common.constants import TokenType
from ...common.schemas import AppoBaseModel


class TokenData(AppoBaseModel):
    username: str
    token_type: TokenType


class Authorize:
    def __init__(
        self,
        username: str = Form(...),
        password: str = Form(...),
        user_agent: str | None = Header(None),
    ):
        self.username = username
        self.password = password
        self.user_agent = user_agent


class TokenResponse(AppoBaseModel):
    access_token: str
    refresh_token: str
    token_type: str = 'bearer'


class CreateManagerRequest(AppoBaseModel):
    name: str
    phone_number: str
    username: str
    password: str

    @validator('name')
    def validate_name(cls, v):
        if len(v) < 2:
            raise ValueError('name must be at least 2 characters long')
        return v

    @validator('username')
    def validate_username(cls, v):
        if len(v) < 8:
            raise ValueError('username must be at least 8 characters long')
        return v

    @validator('password')
    def validate_password(cls, v):
        if len(v) < 8:
            raise ValueError('Password must be at least 8 characters long')
        if not re.search(r'[A-Z]', v):
            raise ValueError('Password must contain at least one uppercase letter')
        if not re.search(r'[a-z]', v):
            raise ValueError('Password must contain at least one lowercase letter')
        if not re.search(r'[0-9]', v):
            raise ValueError('Password must contain at least one digit')
        if not re.search(r'[!@#$%^&*(),.?\":{}|<>]', v):
            raise ValueError('Password must contain at least one special character')
        return v
