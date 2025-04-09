from typing import Type
from pydantic import BaseModel
from public_service.api import Api


class Adapter:
    _api: Api

    def attach(
        self, port_schema: Type[BaseModel], adapter_payload: BaseModel
    ) -> BaseModel:
        return port_schema.model_validate(adapter_payload, from_attributes=False)
