from sqlalchemy import select
from sqlalchemy.orm import Session

from ...models import CounselApplications
from ..schemas import counsel_schema as schema


def get_counsel_applications(
    request: schema.CounselApplicationRequest, db: Session
) -> list[CounselApplications]:
    stmt = select(CounselApplications).where(
        CounselApplications.is_active.is_(True),
        CounselApplications.apartment_id == request.apartment_id,
    )

    if request.name:
        stmt = stmt.where(CounselApplications.name.ilike(f'%{request.name}%'))
    if request.phone_number:
        stmt = stmt.where(
            CounselApplications.phone_number.ilike(f'%{request.phone_number}%')
        )
    if request.gender:
        stmt = stmt.where(CounselApplications.gender.ilike(f'%{request.gender}%'))

    result: list[CounselApplications] = db.scalars(stmt).all()
    return result


def create_counsel_application(
    request: schema.CreateCounselApplicationRequest, db: Session
) -> CounselApplications:
    new_counsel_applications = CounselApplications(
        name=request.name,
        phone_number=request.phone_number,
        gender=request.gender,
        memo=request.memo,
        apartment_id=request.apartment_id,
    )
    db.add(new_counsel_applications)
    db.commit()

    return new_counsel_applications
