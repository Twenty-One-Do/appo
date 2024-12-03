import jwt
from fastapi import Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session

from appo_api.config import settings
from appo_api.core.security import create_jwt
from appo_api.exceptions import UnAuthorizedException

from ...common.constants import TokenType
from ..cruds import login_crud as crud
from ..schemas import login_schemas as schema


def login(authorize: schema.Authorize, db: Session) -> schema.TokenResponse:
    manager = crud.get_user_by_login_id(authorize.username, db)
    if not manager.is_active:
        raise UnAuthorizedException(detail='inactive manager')
    if not manager.verify_password(authorize.password):
        raise UnAuthorizedException(detail='invalid password')
    access_token = create_jwt(
        {'username': manager.username, 'token_type': TokenType.ACCESS},
        expires=settings.ACCESS_TOKEN_EXPIRE_MINUTES,
    )
    refresh_token = create_jwt(
        {'username': manager.username, 'token_type': TokenType.REFRESH},
        expires=settings.REFRESH_TOKEN_EXPIRE_MINUTES,
    )
    return schema.TokenResponse(access_token=access_token, refresh_token=refresh_token)


def refresh(refresh_token: str, db: Session) -> schema.TokenResponse:
    token_data = _parse_token(refresh_token)
    if token_data.token_type != TokenType.REFRESH:
        raise UnAuthorizedException(detail='invalid token')

    manager = crud.get_user_by_login_id(token_data.username, db)
    if not manager.is_active:
        raise UnAuthorizedException(detail='inactive manager')

    new_access_token = create_jwt(
        {
            'username': manager.username,
            'token_type': TokenType.ACCESS,
        },
        expires=settings.ACCESS_TOKEN_EXPIRE_MINUTES,
    )
    new_refresh_token = create_jwt(
        {
            'username': manager.username,
            'token_type': TokenType.REFRESH,
        },
        expires=settings.REFRESH_TOKEN_EXPIRE_MINUTES,
    )

    return schema.TokenResponse(
        access_token=new_access_token, refresh_token=new_refresh_token
    )


def _parse_token(token: str) -> schema.TokenData:
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        username = payload.get('username')
        token_type = payload.get('token_type')
        if not username or not token_type:
            raise UnAuthorizedException(detail={'error': 'missing_payload'})
    except jwt.ExpiredSignatureError as e:
        raise UnAuthorizedException(
            detail={'error': 'token_expired', 'debug': str(e)}
        ) from e
    except jwt.PyJWTError as e:
        raise UnAuthorizedException(
            detail={'error': 'token_invalid', 'debug': str(e)}
        ) from e

    return schema.TokenData(username=username, token_type=token_type)


def verify_token(
    credentials: HTTPAuthorizationCredentials | None = Security(
        HTTPBearer(auto_error=False)
    ),
) -> schema.TokenData:
    """
    유효한 JWT인지 체크, 인가(Authorization), scope 단위로 권한 체크
    """
    if not credentials:
        raise UnAuthorizedException(detail='no credentials')

    token_data = _parse_token(credentials.credentials)
    if token_data.token_type != TokenType.ACCESS:
        raise UnAuthorizedException(detail='invalid token type')
    return token_data


def register(request: schema.CreateManagerRequest, db: Session) -> schema.TokenResponse:
    manager = crud.register(request, db)

    access_token = create_jwt(
        {'username': manager.username, 'token_type': TokenType.ACCESS},
        expires=settings.ACCESS_TOKEN_EXPIRE_MINUTES,
    )
    refresh_token = create_jwt(
        {'username': manager.username, 'token_type': TokenType.REFRESH},
        expires=settings.REFRESH_TOKEN_EXPIRE_MINUTES,
    )
    return schema.TokenResponse(access_token=access_token, refresh_token=refresh_token)
