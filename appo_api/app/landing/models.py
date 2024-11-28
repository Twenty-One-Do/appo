from sqlalchemy import Uuid, Integer, String, DateTime, ForeignKey, Enum
from sqlalchemy.orm import (
    DeclarativeBase,
    registry,
    Mapped,
    mapped_column,
    relationship,
)
from datetime import datetime, timezone
import enum
import uuid


class Base(DeclarativeBase):
    registry = registry(
        type_annotation_map={
            str: String(255),
            uuid.UUID: Uuid,
        }
    )


class DateMixin:
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=lambda: datetime.now(timezone.utc)
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )


class Gender(enum.Enum):
    male = "male"
    female = "female"


class CounselApplication(Base, DateMixin):
    __tablename__ = "counsels"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, index=True, nullable=False
    )
    name: Mapped[str] = mapped_column(String(40), nullable=False)
    phone_number: Mapped[str] = mapped_column(String(20), nullable=False)
    gender: Mapped[Gender] = mapped_column(Enum(Gender), nullable=True)
    memo: Mapped[str] = mapped_column(String(500), nullable=True)
    apartment_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("apartments.id"), index=True, nullable=False
    )

    apartment = relationship("Apartment", back_populates="counsel_applications")
