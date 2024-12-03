from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from appo_api.core.database import get_db

from ..schemas import counsel_schema as schema
from ..services import counsel_service as service

router = APIRouter(prefix='/landing', tags=['landing'])


@router.get(
    '/counsel/application',
    summary='상담 신청 조회',
    response_model=list[schema.CounselApplicationResponse],
)
def get_counsel_application(
    request: schema.CounselApplicationRequest,
    db: Session = Depends(get_db),
):
    return service.get_counsel_application(request=request, db=db)


@router.post(
    '/counsel/application',
    summary='상담 신청 생성',
    response_model=schema.CounselApplicationResponse,
)
def create_counsel_application(
    request: schema.CreateCounselApplicationRequest,
    db: Session = Depends(get_db),
):
    return service.create_counsel_application(request=request, db=db)
