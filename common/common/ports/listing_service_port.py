from abc import abstractmethod
from common.ports.port import Port
from common.types.schemas import (
    ListingCreateRes,
    ListingListReq,
    ListingListRes,
    ListingCreateReq,
)


class ListingServicePort(Port):
    @abstractmethod
    def list(self, q: ListingListReq) -> ListingListRes:
        pass

    @abstractmethod
    def create_listing(self, payload: ListingCreateReq) -> ListingCreateRes:
        pass
