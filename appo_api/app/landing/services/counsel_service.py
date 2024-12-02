from sqlalchemy.orm import Session

from ..cruds import counsel_crud as crud
from ..schemas import counsel_schema as schema


def create_counsel_application(
    request: schema.CounselApplicationRequest, db: Session
) -> schema.CounselApplicationResponse:
    counsel_application = crud.create_counsel_application(request, db)
    return schema.CounselApplicationResponse.from_orm(counsel_application)
