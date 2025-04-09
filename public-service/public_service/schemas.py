from typing import List, Optional
from pydantic import BaseModel, Field


class BaseResponse(BaseModel):
    result: bool


class Pagination(BaseModel):
    page_num: int = Field(1, gt=0)
    page_size: int = Field(10, gt=0)


class QueryParameter(Pagination):
    user_id: Optional[int] = None


class UserSchema(BaseModel):
    id: int
    name: str
    created_at: int
    updated_at: int


class ListingSchema(BaseModel):
    id: int
    listing_type: str
    price: int
    created_at: int
    updated_at: int
    user: UserSchema


class Listing(BaseResponse):
    listings: List[ListingSchema]


class UserCreate(BaseModel):
    name: str


class UserCreateResponse(BaseModel):
    user: UserSchema


class ListingCreate(BaseModel):
    user_id: int
    listing_type: str
    price: int


class ListingCreateResponse(BaseModel):
    listing: ListingSchema
