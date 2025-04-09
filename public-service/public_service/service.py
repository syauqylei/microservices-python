from typing import Any
from common.types.schemas import ListingCreateReq, ListingListReq, UserCreateReq
from common.utils import create_log
from public_service.adapters.listing_service_adapter import ListingServiceAdapter
from public_service.adapters.user_service_adapter import UserServiceAdapter
from public_service.schemas import (
    ListingCreate,
    ListingCreateResponse,
    ListingListRequest,
    ListingListResponse,
    UserCreate,
    UserCreateResponse,
)


class PublicService:
    _user_service: UserServiceAdapter
    _listing_service: ListingServiceAdapter
    _log: Any

    def __init__(self):
        self._listing_service = ListingServiceAdapter()
        self._user_service = UserServiceAdapter()
        self._log = create_log(self.__class__.__name__)

    def create_user(self, payload: UserCreate) -> UserCreateResponse:
        self._log.info("Validating Payload", payload=payload)
        data = UserCreateReq.model_validate(payload, from_attributes=True)

        self._log.info("Payload", payload=payload)
        ret = self._user_service.create_user(data)
        return UserCreateResponse.model_validate(ret, from_attributes=True)

    def create_listing(self, payload: ListingCreate) -> ListingCreateResponse:
        self._log.info("Validating Payload", payload=payload)
        data = ListingCreateReq.model_validate(payload, from_attributes=True)

        ret = self._listing_service.create_listing(data)

        self._log.info("Result", result=ret)
        return ListingCreateResponse.model_validate(ret, from_attributes=True)

    def list_listing(self, payload: ListingListRequest) -> ListingListResponse:
        self._log.info("Validating Payload", payload=payload)
        data = ListingListReq.model_validate(payload, from_attributes=True)

        self._log.info("Payload", payload=payload)
        ret = self._listing_service.list(data)
        return ListingListResponse.model_validate(ret, from_attributes=True)
