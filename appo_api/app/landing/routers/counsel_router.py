from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from appo_api.core.database import get_db

from ..schemas import counsel_schema as schema
from ..services import counsel_service as service

router = APIRouter(prefix='/landing', tags=['landing'])


@router.post(
    '/counsel/application',
    summary='상담 신청',
    response_model=schema.CounselApplicationResponse,
)
def create_counsel_application(
    request: schema.CounselApplicationRequest,
    db: Session = Depends(get_db),
):
    return service.create_counsel_application(request=request, db=db)
