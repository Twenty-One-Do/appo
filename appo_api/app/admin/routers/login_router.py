from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.params import Form
from sqlalchemy.orm import Session

from appo_api.core.database import get_db

from ..schemas import login_schemas as schema
from ..services import login_service

router = APIRouter(prefix='/admin', tags=['admin'])


@router.post(
    '/login',
    summary='로그인',
    description='로그인',
    response_model=schema.TokenResponse,
)
def login(authorize: schema.Authorize = Depends(), db: Session = Depends(get_db)):
    return login_service.login(authorize, db)


@router.post(
    '/refresh',
    summary='토큰 갱신',
    description='토큰 갱신',
    response_model=schema.TokenResponse,
)
def refresh(refresh_token: Annotated[str, Form()], db: Session = Depends(get_db)):
    return login_service.refresh(refresh_token, db)


@router.post(
    '/register',
    summary='매니저 등록',
    description='매니저 등록',
    response_model=schema.TokenResponse,
)
def register(
    request: schema.CreateManagerRequest,
    db: Session = Depends(get_db),
):
    return login_service.register(request, db)
