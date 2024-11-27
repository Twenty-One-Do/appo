
from ..cruds import apt_crud as crud
from ..schemas import apt_schema as schema

def get_apt_info(
    request: schema.AptInfoRequest,
    db: Session
) -> None:
    apt_info = crud.get_apt_info(db)
    return None