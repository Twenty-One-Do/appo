import uuid
from sqlalchemy import Integer, String, Boolean, Uuid
from datetime import datetime, timezone
from sqlalchemy.orm import DeclarativeBase, registry, mapped_column, Mapped


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
