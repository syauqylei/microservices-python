from enum import Enum
from typing import List, Optional

from pydantic import BaseModel
from common.types import CommonField, Pagination, Response


class User(CommonField):
    name: str


class UserListReq(Pagination):
    pass


class UserListRes(Response):
    users: List[User]


class UserViewRes(Response):
    user: User


class UserCreateReq(BaseModel):
    name: str


class UserCreateRes(UserViewRes):
    pass


class ListingType(str, Enum):
    RENT = "rent"
    SALE = "sale"


class Listing(CommonField):
    user_id: int
    listing_type: ListingType
    price: int


class ListingListReq(Pagination):
    user_id: Optional[int] = None


class ListingListRes(Response):
    listings: List[Listing]


class ListingCreateReq(BaseModel):
    user_id: int
    listing_type: str
    price: int


class ListingCreateRes(Response):
    listing: Listing
