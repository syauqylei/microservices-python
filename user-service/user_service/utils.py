from typing import Any, Tuple, Type, TypeVar

from sqlalchemy import Select
from sqlmodel import select

from user_service.model import Base
from user_service.schemas import Pagination

T = TypeVar("T")
TModel = TypeVar("TModel", bound=Base)


class QueryHandler[TModel]:
    _stmt: Select[Tuple[TModel]]
    _model: Type[TModel]

    def __init__(self, model: Type[TModel]):
        self._model = model
        self._stmt = select(model)

    def _paginate(self, page_num: int, page_size: int):
        limit = page_num * page_size
        offset = (page_num - 1) * page_size

        self._stmt = self._stmt.limit(limit).offset(offset)

    def queryPage(self, pagination: Pagination):
        self._paginate(page_num=pagination.page_num, page_size=pagination.page_size)
        return self._stmt

    def get_by_id(self, model_id: int):
        self._stmt = self._stmt.where(self._model.id == model_id)
        return self._stmt
