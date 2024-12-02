from sqlalchemy.orm import Session

from ...models import CounselApplications
from ..schemas import counsel_schema as schema


def create_counsel_application(
    request: schema.CounselApplicationRequest, db: Session
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
