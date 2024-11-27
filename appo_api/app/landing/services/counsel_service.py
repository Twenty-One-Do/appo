from ..cruds import counsel_crud as crud
from ..schemas import counsel_schema as schema

def create_counsel_application(
    request: schema.CounselApplicationRequest,
    db: Session
) -> None:
    crud.create_counsel_application(db)
    return None