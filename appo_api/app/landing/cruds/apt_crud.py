from sqlalchemy import select
from sqlalchemy.orm import Session

from ...models import ApartmentInfos
from ..schemas import apt_schema as schema


def get_apt_info(
    request: schema.AptInfoRequest,
    db: Session,
) -> list[ApartmentInfos]:
    stmt = select(ApartmentInfos).where(ApartmentInfos.is_active.is_(True))

    if request.apt_info_id:
        stmt = stmt.where(ApartmentInfos.id == request.apt_info_id)
    if request.name:
        stmt = stmt.where(ApartmentInfos.name.ilike(f'%{request.name}%'))
    if request.main_number:
        stmt = stmt.where(ApartmentInfos.main_number.ilike(f'%{request.main_number}%'))
    if request.location:
        stmt = stmt.where(ApartmentInfos.location.ilike(f'%{request.location}%'))
    if request.company:
        stmt = stmt.where(ApartmentInfos.company.ilike(f'%{request.company}%'))

    result: list[ApartmentInfos] = db.scalars(stmt).all()
    return result


def create_apt_info(
    request: schema.CreateAptInfoRequest,
    db: Session,
) -> ApartmentInfos:
    new_apartment_infos = ApartmentInfos(
        name=request.name,
        main_number=request.main_number,
        location=request.location,
        company=request.company,
        introduction=request.introduction,
    )
    db.add(new_apartment_infos)
    db.commit()

    return new_apartment_infos
