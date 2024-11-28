from ...common.schemas import AppoBaseModel
from typing import Optional


class AptInfoRequest(AppoBaseModel):
    name: str
    main_number: str
    location: str
    company_id: int
    introduction: Optional[str] = None
    is_active: Optional[bool] = True


class AptInfoResponse(AppoBaseModel):
    id: int
    name: str
    main_number: str
    location: str
    company_id: int
    introduction: Optional[str] = None
    is_active: bool
