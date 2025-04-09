from re import S
from typing import Annotated
from fastapi import APIRouter, Body, Query

from public_service.schemas import (
    Listing,
    ListingCreate,
    ListingCreateResponse,
    QueryParameter,
    UserCreate,
    UserCreateResponse,
)


router = APIRouter(prefix="/public-listing")


@router.get("/listings", tags=["Public API Listing"])
def list(q: Annotated[QueryParameter, Query()]):
    return Listing.model_validate(
        {
            "result": True,
            "listings": [
                {
                    "id": 1,
                    "listing_type": "rent",
                    "price": 6000,
                    "created_at": 1475820997000000,
                    "updated_at": 1475820997000000,
                    "user": {
                        "id": 1,
                        "name": "Suresh Subramaniam",
                        "created_at": 1475820997000000,
                        "updated_at": 1475820997000000,
                    },
                }
            ],
        }
    )


@router.post("/users", tags=["Public API User"])
def add_user(user: Annotated[UserCreate, Body(embed=True)]):
    return UserCreateResponse.model_validate(
        {
            "user": {
                "id": 1,
                "name": "Lorel Ipsum",
                "created_at": 1475820997000000,
                "updated_at": 1475820997000000,
            }
        }
    )


@router.post("/listings", tags=["Public API Listing"])
def add_listing(listing: Annotated[ListingCreate, Body(embed=True)]):
    return ListingCreateResponse.model_validate(
        {
            "listing": {
                "id": 143,
                "user_id": 1,
                "listing_type": "rent",
                "price": 6000,
                "created_at": 1475820997000000,
                "updated_at": 1475820997000000,
            }
        }
    )
