from typing import Annotated
from fastapi import APIRouter, Depends, Form, HTTPException, Query

from user_service import create_logger
from user_service.schemas import (
    Pagination,
    UserCreate,
    UserCreateRes,
    UserListRes,
    UserRetrieveRes,
)
from user_service.service import UserService

route = APIRouter(prefix="/users")

Log = create_logger("user_service", "route")


@route.get("", tags=["Users"], response_model=UserListRes)
def list(
    q: Annotated[Pagination, Query()], service: UserService = Depends()
) -> UserListRes:
    Log.info(f"list - {q}")
    ret = None

    try:
        ret = service.find_page(q)
    except Exception as e:
        Log.error(e)

    if not ret:
        raise HTTPException(status_code=500, detail="Internal Server Error")

    Log.info(f"result - {ret}")
    return UserListRes(result=bool(ret), users=ret)


@route.get("/{user_id}", tags=["Users"], response_model=UserRetrieveRes)
def retrieve(user_id: int, service: UserService = Depends()) -> UserRetrieveRes:
    Log.info(f"Get user by id = {user_id}")
    ret = None
    try:
        ret = service.get_by_id(user_id)
    except Exception as e:
        Log.error(e)

    if not ret:
        raise HTTPException(status_code=500, detail="Internal Server Error")

    return UserRetrieveRes(result=bool(ret), user=ret)


@route.post("", tags=["Users"], response_model=UserCreateRes)
def add(q: Annotated[UserCreate, Form()], service: UserService = Depends()):
    Log.info("add user", q)

    user = None

    try:
        user = service.create_user(q.name)
    except Exception as e:
        Log.error(f"Error: creating user {q.model_dump_json()}")

    if not user:
        raise HTTPException(
            status_code=400, detail=f"Error: creating user: {q.model_dump_json()} "
        )
    return UserCreateRes(result=bool(user), user=user)
