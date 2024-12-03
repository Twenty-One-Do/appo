from sqlalchemy.orm import Session

from ..cruds import apt_crud as crud
from ..schemas import apt_schema as schema


def get_apt_info(
    request: schema.AptInfoRequest, db: Session
) -> list[schema.AptInfoResponse]:
    apt_infos = crud.get_apt_info(
        request,
        db,
    )
    return [schema.AptInfoResponse.from_orm(apt_info) for apt_info in apt_infos]


def create_apt_info(
    request: schema.CreateAptInfoRequest, db: Session
) -> schema.AptInfoResponse | bool:
    apt_info = crud.create_apt_info(
        request=request,
        db=db,
    )
    if apt_info:
        return schema.AptInfoResponse.from_orm(apt_info)
    else:
        return False
