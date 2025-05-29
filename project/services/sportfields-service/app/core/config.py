# from pydantic import BaseSettings, Field

# class Settings(BaseSettings):
#     DATABASE_URL: str = Field(..., env="DATABASE_URL")
#     JWT_SECRET: str = Field(..., env="JWT_SECRET")
#     ALGORITHM: str = "HS256"
#     ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

#     class Config:
#         env_file = ".env"
#         env_file_encoding = "utf-8"

# settings = Settings()

# app/core/config.py

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DATABASE_URL: str = Field(..., env="DATABASE_URL")
    JWT_SECRET:    str = Field(..., env="JWT_SECRET")
    ALGORITHM:     str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    # Tell BaseSettings where to load .env from
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8"
    )

settings = Settings()
