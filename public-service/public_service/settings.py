from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSetting(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    user_service_url: str = Field(
        alias="USER_SERVICE_URL", default="http://localhost:8001"
    )
    listing_service_url: str = Field(
        alias="LISTING_SERVICE_URL", default="http://localhost:8000"
    )


AppConfig = AppSetting()
