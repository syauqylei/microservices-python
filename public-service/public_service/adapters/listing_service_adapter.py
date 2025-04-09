from common.ports.listing_service_port import ListingServicePort
from common.types.schemas import (
    ListingCreateReq,
    ListingCreateRes,
    ListingListReq,
    ListingListRes,
)
from common.utils import create_log
from fastapi import HTTPException
import requests
from public_service.adapters.adapter import Adapter
from public_service.api import Api
from public_service.settings import AppConfig

LOG = create_log(__name__)


class ListingServiceAdapter(ListingServicePort, Adapter):
    def __init__(self) -> None:
        self._api = Api(AppConfig.listing_service_url)

    def create_listing(self, payload: ListingCreateReq) -> ListingCreateRes:
        ret = None
        error = None
        LOG.info("Request - Create Listing", payload=payload)

        try:
            ret = requests.post(
                "http://localhost:8000/listings", data=payload.model_dump()
            )
            LOG.info("Request - Create Listing", payload=payload, response=ret.json())
        except Exception as e:
            error = e
            LOG.error("Error - Create Listing", e=e)

        if not ret:
            raise HTTPException(status_code=500, detail=error)
        return ListingCreateRes(**ret.json())

    def list(self, q: ListingListReq) -> ListingListRes:
        ret = None
        error = None
        LOG.info("Request - List Listing", params=q.model_dump())

        try:
            ret = requests.get("http://localhost:8000/listings", params=q.model_dump())
            LOG.info(
                "Request - List Listing", params=q.model_dump(), response=ret.json()
            )
        except Exception as e:
            error = e
            LOG.error("Error - List Listing", e=e)

        if not ret:
            raise HTTPException(status_code=500, detail=error)
        return ListingListRes(**ret.json())
