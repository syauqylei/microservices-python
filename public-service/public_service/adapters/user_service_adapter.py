from common.utils import create_log
from common.ports.user_service_port import UserServicePort
from common.types.schemas import UserCreateReq, UserCreateRes
from fastapi import HTTPException

from public_service.adapters.adapter import Adapter
from public_service.api import Api
from public_service.settings import AppConfig

LOG = create_log(__name__)


class UserServiceAdapter(UserServicePort, Adapter):
    def __init__(self) -> None:
        self._api = Api(AppConfig.user_service_url)

    def create_user(self, payload: UserCreateReq) -> UserCreateRes:
        ret = None
        error = None
        LOG.info("Request - Create User", payload=payload)

        try:
            ret = self._api.post("/users", {"name": payload.name})
            LOG.info("Request - Create User", payload=payload, response=ret.json())
        except Exception as e:
            error = e
            LOG.error("Error - Create User", e=e)

        if not ret:
            raise HTTPException(status_code=500, detail=error)
        return UserCreateRes(**ret.json())
