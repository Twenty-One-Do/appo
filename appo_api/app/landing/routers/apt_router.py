from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from appo_api.core.database import get_db

from ..schemas import apt_schema as schema
from ..services import apt_service as service

router = APIRouter(prefix='landing', tags=['landing'])


@router.get(
    '/apt/info', summary='아파트 랜딩페이지 정보', response_model=schema.AptInfoResponse
)
def get_apt_info(
    request: schema.AptInfoRequest = Depends(schema.AptInfoRequest),
    db: Session = Depends(get_db),
):
    return service.get_apt_info(request, db=db)
