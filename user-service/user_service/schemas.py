from typing import List
from pydantic import BaseModel, Field

from user_service.model import Base, User


class Pagination(BaseModel):
    page_num: int = Field(1, gt=0)
    page_size: int = Field(10, gt=0)


class BaseResponse(BaseModel):
    result: bool


class UserListRes(BaseResponse):
    users: List[User]


class UserRetrieveRes(BaseResponse):
    user: User


class UserCreate(BaseModel):
    name: str


class UserCreateRes(BaseResponse):
    user: User
