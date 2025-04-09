from typing import List, Type
from fastapi import Depends
from sqlmodel import Session
from sqlalchemy import select
from user_service import create_logger
from user_service.database import get_session
from user_service.model import User
from user_service.schemas import Pagination
from user_service.utils import QueryHandler


Log = create_logger("user_service", "UserService")


class UserService:
    _session: Session
    _queryHandler: QueryHandler
    _model: Type[User]

    def __init__(self, model: Type = User, session: Session = Depends(get_session)):
        self._session = session
        self._model = model
        self._queryHandler = QueryHandler(model)

    def create_user(self, name) -> User:
        user = User(name=name)
        Log.info(f"Create user {name}", user.model_dump())

        self._session.add(user)
        self._session.commit()
        self._session.refresh(user)

        Log.info(f"Created user {name}", user.model_dump())
        return self._model.model_validate(user.model_dump())

    def find_page(self, pagination: Pagination) -> List[User]:
        Log.info(f"Query users { pagination.model_dump_json()}")

        stmt = self._queryHandler.queryPage(pagination)
        rows = self._session.scalars(stmt).all()

        Log.info(f"Result = {rows[:5]} count = {len(rows)}")

        return [self._model.model_validate(row, strict=False) for row in rows]

    def get_by_id(self, user_id: int) -> User:
        stmt = self._queryHandler.get_by_id(user_id)
        Log.info(f"Query = {stmt}")
        row = self._session.scalar(stmt)
        return self._model.model_validate(row, strict=False)
