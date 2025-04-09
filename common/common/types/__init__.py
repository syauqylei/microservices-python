from pydantic import BaseModel


class Pagination(BaseModel):
    page_num: int
    page_size: int


class CommonField(BaseModel):
    id: int
    created_at: int
    updated_at: int


class Response(BaseModel):
    result: bool
