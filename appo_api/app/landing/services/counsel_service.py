from sqlalchemy.orm import Session

from ..cruds import counsel_crud as crud
from ..schemas import counsel_schema as schema


def get_counsel_application(
    request: schema.CounselApplicationRequest, db: Session
) -> list[schema.CounselApplicationResponse]:
    counsel_applications = crud.get_counsel_applications(request, db)
    return [
        schema.CounselApplicationResponse.from_orm(counsel_application)
        for counsel_application in counsel_applications
    ]


def create_counsel_application(
    request: schema.CreateCounselApplicationRequest, db: Session
) -> schema.CounselApplicationResponse:
    counsel_application = crud.create_counsel_application(request, db)
    return schema.CounselApplicationResponse.from_orm(counsel_application)
