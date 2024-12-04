from sqlalchemy import select
from sqlalchemy.orm import Session

from appo_api.exceptions import UserNotFound

from ...models import Managers
from ..schemas import login_schemas as schema


def get_user_by_login_id(username: str, db: Session):
    manager = db.query(Managers).filter(Managers.username == username).first()
    if not manager:
        raise UserNotFound(detail={'username': username})

    return manager


def register(request: schema.CreateManagerRequest, db: Session) -> Managers:
    new_manager = Managers(
        name=request.name, phone_number=request.phone_number, username=request.username
    )
    new_manager.set_password(request.password)

    db.add(new_manager)
    db.commit()

    return new_manager


def get_manager_by_number(
    request: schema.CreateManagerRequest, db: Session
) -> list[Managers] | None:
    stmt = select(Managers).where(
        Managers.is_active.is_(True),
        Managers.phone_number == request.phone_number,
    )

    result: list[Managers] | None = db.scalars(stmt).all()
    return result


def get_manager_by_username(
    request: schema.CreateManagerRequest, db: Session
) -> list[Managers] | None:
    stmt = select(Managers).where(
        Managers.is_active.is_(True),
        Managers.username == request.username,
    )

    result: list[Managers] | None = db.scalars(stmt).all()
    return result
