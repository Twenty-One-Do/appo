from sqlalchemy import select
from sqlalchemy.orm import Session

from ...models import ApartmentInfos


def get_apt_info(
    apt_info_id: int,
    name: str | None,
    main_number: str | None,
    location: str | None,
    company: str | None,
    db: Session,
) -> ApartmentInfos | None:
    stmt = select(ApartmentInfos).where(
        ApartmentInfos.is_active.is_(True), ApartmentInfos.id == apt_info_id
    )

    # if name:
    #     stmt = stmt.where(ApartmentInfos.name.ilike(f"%{name}%"))
    # if main_number:
    #     stmt = stmt.where(ApartmentInfos.main_number.ilike(f"%{main_number}%"))
    # if location:
    #     stmt = stmt.where(ApartmentInfos.location.ilike(f"%{location}%"))
    # if company:
    #     stmt = stmt.where(ApartmentInfos.company.ilike(f"%{company}%"))

    result: ApartmentInfos | None = db.scalars(stmt).first()
    return result
