from datetime import datetime

from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel

from .utils import to_utc_isoformat


class AppoBaseModel(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True, json_encoders={datetime: to_utc_isoformat})
    apt_branch: str | None = None
