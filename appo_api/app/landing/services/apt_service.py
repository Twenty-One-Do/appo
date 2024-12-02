from sqlalchemy.orm import Session

from ..cruds import apt_crud as crud
from ..schemas import apt_schema as schema


def get_apt_info(
    request: schema.AptInfoRequest, db: Session
) -> schema.AptInfoResponse | bool:
    apt_info = crud.get_apt_info(
        apt_info_id=request.apt_info_id,
        name=request.name,
        main_number=request.main_number,
        location=request.location,
        company=request.company,
        db=db,
    )
    if apt_info:
        return schema.AptInfoResponse.from_orm(apt_info)
    else:
        return False
