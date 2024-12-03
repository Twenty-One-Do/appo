from typing import Self

from ...common.schemas import AppoBaseModel
from ...models import ApartmentInfos


class AptInfoRequest(AppoBaseModel):
    apt_info_id: int | None = None
    name: str | None = None
    main_number: str | None = None
    location: str | None = None
    company: str | None = None


class CreateAptInfoRequest(AppoBaseModel):
    name: str
    main_number: str
    location: str | None = None
    company: str | None = None
    introduction: str | None = None


class AptInfoResponse(AppoBaseModel):
    apt_info_id: int
    name: str
    main_number: str
    location: str | None = None
    company: str | None = None
    introduction: str | None = None
    is_active: bool

    @classmethod
    def from_orm(cls, aptinfo: ApartmentInfos) -> Self:
        return cls(
            apt_info_id=aptinfo.id,
            name=aptinfo.name,
            main_number=aptinfo.main_number,
            location=aptinfo.location,
            company=aptinfo.company,
            introduction=aptinfo.introduction,
            is_active=aptinfo.is_active,
        )
