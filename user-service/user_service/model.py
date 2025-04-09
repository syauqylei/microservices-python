import datetime
from sqlmodel import SQLModel, Field


def now_bigint() -> int:
    now = datetime.datetime.now()
    return int(now.timestamp() * 1_000_000)


class Base(SQLModel):
    id: int = Field(default=None, primary_key=True)
    created_at: int = Field(
        default_factory=now_bigint,
    )
    updated_at: int = Field(
        default_factory=now_bigint,
    )


class User(Base, table=True):
    __tablename__ = "users"

    name: str
