from abc import abstractmethod

from common.ports.port import Port
from common.types.schemas import (
    UserCreateReq,
    UserCreateRes,
    UserListReq,
    UserListRes,
    UserViewRes,
)


class UserServicePort(Port):
    @abstractmethod
    def list(self, pagination: UserListReq) -> UserListRes:
        pass

    @abstractmethod
    def view(self, user_id: int) -> UserViewRes:
        pass

    @abstractmethod
    def create_user(self, payload: UserCreateReq) -> UserCreateRes:
        pass
