from typing import Self

from ...common.constants import Gender
from ...common.schemas import AppoBaseModel
from ...models import CounselApplications


class CounselApplicationRequest(AppoBaseModel):
    name: str | None = None
    phone_number: str | None = None
    gender: Gender | None = None
    memo: str | None = None
    apartment_id: int


class CreateCounselApplicationRequest(AppoBaseModel):
    name: str
    phone_number: str
    gender: Gender | None = None
    memo: str | None = None
    apartment_id: int


class CounselApplicationResponse(AppoBaseModel):
    application_id: int
    name: str
    phone_number: str
    gender: Gender | None = None
    memo: str | None = None
    apartment_id: int
    is_active: bool

    @classmethod
    def from_orm(cls, counsel_application: CounselApplications) -> Self:
        return cls(
            application_id=counsel_application.id,
            name=counsel_application.name,
            phone_number=counsel_application.phone_number,
            gender=counsel_application.gender,
            memo=counsel_application.memo,
            apartment_id=counsel_application.apartment_id,
            is_active=counsel_application.is_active,
        )
