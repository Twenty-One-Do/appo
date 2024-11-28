import uuid
from datetime import datetime, timezone

from sqlalchemy import Boolean, Enum, ForeignKey, Integer, String, Uuid
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    registry,
)
from werkzeug.security import check_password_hash, generate_password_hash

from appo_api.app.common.constants import Gender


class Base(DeclarativeBase):
    registry = registry(
        type_annotation_map={
            str: String(255),
            uuid.UUID: Uuid,
        }
    )


class Basic:
    created_at: Mapped[datetime] = mapped_column(
        default=lambda: datetime.now(timezone.utc)
    )
    updated_at: Mapped[datetime] = mapped_column(
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)


class ApartmentInfos(Base, Basic):
    __tablename__ = 'apartment_infos'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(40), nullable=False)
    main_number: Mapped[str] = mapped_column(String(13), nullable=False)
    location: Mapped[str] = mapped_column(String(200), nullable=True)
    company: Mapped[str] = mapped_column(String(40), nullable=True)
    introduction: Mapped[str] = mapped_column(String(500), nullable=True)


class CounselApplications(Base, Basic):
    __tablename__ = 'counsel_applications'

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, index=True, nullable=False
    )
    name: Mapped[str] = mapped_column(String(40), nullable=False, default='익명')
    phone_number: Mapped[str] = mapped_column(String(20), nullable=False)
    gender: Mapped[Gender] = mapped_column(Enum(Gender), nullable=True)
    memo: Mapped[str] = mapped_column(String(500), nullable=True)
    apartment_id: Mapped[int] = mapped_column(
        Integer, ForeignKey('apartment_infos.id'), index=True, nullable=False
    )


class ManagerApartmentMap(Base, Basic):
    __tablename__ = 'manager_apartment_map'

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, index=True, nullable=False
    )
    manager_id: Mapped[int] = mapped_column(
        Integer, ForeignKey('managers.id'), index=True, nullable=False
    )
    apartment_id: Mapped[int] = mapped_column(
        Integer, ForeignKey('apartment_infos.id'), index=True, nullable=False
    )


class Managers(Base, Basic):
    __tablename__ = 'managers'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(40), nullable=False)
    phone_number: Mapped[str] = mapped_column(String(13), nullable=False)
    username: Mapped[str] = mapped_column(String(40), nullable=False)
    password: Mapped[str] = mapped_column(String(40), nullable=False)

    def set_password(self, password: str) -> None:
        self.password = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        result: bool = check_password_hash(self.hashed_password, password)
        return result
