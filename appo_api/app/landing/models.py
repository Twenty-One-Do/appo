from sqlalchemy import Uuid, Integer, String, Enum, Boolean
from sqlalchemy.orm import (
    DeclarativeBase,
    registry,
    Mapped,
    mapped_column,
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
    created_at = Mapped[datetime] = mapped_column(
        default=lambda: datetime.now(timezone.utc)
    )
    updated_at: Mapped[datetime] = mapped_column(
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )


class Apartment(Base, DateMixin):
    __tablename__ = "apartments"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(40), nullable=False)
    main_number: Mapped[str] = mapped_column(String(13), nullable=False)
    location: Mapped[str] = mapped_column(String(200), nullable=False)
    company: Mapped[str] = mapped_column(String(40), nullable=False)
    introduction: Mapped[str] = mapped_column(String(500), nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    # counsels: Mapped[list["Counsel"]] = relationship(
    #     "Counsel", back_populates="apartment"
    # )


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
    # apartment_id: Mapped[int] = mapped_column(
    #     Integer, ForeignKey("apartments.id"), index=True, nullable=False
    # )

    # apartment = relationship("Apartment", back_populates="counsel_applications")
