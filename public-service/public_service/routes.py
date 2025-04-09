from typing import Annotated
from fastapi import APIRouter, Body, Depends, Query

from public_service.schemas import (
    ListingCreate,
    ListingListRequest,
    ListingListResponse,
    ListingCreateResponse,
    UserCreate,
    UserCreateResponse,
)
from public_service.service import PublicService


router = APIRouter(prefix="/public-listing")


@router.get(
    "/listings", tags=["Public API Listing"], response_model=ListingListResponse
)
def list(q: Annotated[ListingListRequest, Query()], service: PublicService = Depends()):
    return service.list_listing(q)


@router.post("/users", tags=["Public API User"], response_model=UserCreateResponse)
def add_user(user: Annotated[UserCreate, Body()], service: PublicService = Depends()):
    return service.create_user(user)


@router.post(
    "/listings", tags=["Public API Listing"], response_model=ListingCreateResponse
)
def add_listing(
    payload: Annotated[ListingCreate, Body()], service: PublicService = Depends()
):
    return service.create_listing(payload)
