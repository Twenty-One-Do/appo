from fastapi import APIRouter, Depends
from appo_api.core.database import get_db
from sqlalchemy.orm import Session

from ..services import counsel_service as service
from ..schemas import counsel_schema as schema

router = APIRouter(prefix="landing", tags=["landing"])


@router.get(
    "/counsel/application",
    summary="상담 신청",
    response_model=schema.CounselApplicationResponse,
)
def create_counsel_application(
    request: schema.CounselApplicationRequest = Depends(
        schema.CounselApplicationRequest
    ),
    db: Session = Depends(get_db),
):
    return service.create_counsel_application
