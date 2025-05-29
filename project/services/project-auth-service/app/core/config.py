# from pydantic import BaseSettings



# class Settings (BaseSettings):

#     '''
#         Configuration settings for the application.
#     '''

#     # JWT settings.
#     JWT_SECRET: str
#     JWT_ALGORITHM: str
#     ACCESS_TOKEN_EXPIRE_MINUTES: int
#     REFRESH_TOKEN_EXPIRE_MINUTES: int
#     DATABASE_URL: str


#     class Config:

#         '''
#             Configuration for the Pydantic settings.
#             This specifies that the settings should be loaded from a .env file.
#         '''

#         env_file = ".env"



# # Create an instance of the Settings class to load the configuration.
# settings = Settings()

# app/config.py

from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """
    Configuration settings for the Auth service.
    Loaded from `.env` (or environment) at startup.
    """

    # JWT settings
    JWT_SECRET: str
    JWT_ALGORITHM: str = "HS256"

    # Access tokens live for 15 minutes by default
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 15

    # Refresh tokens live for 7 days by default
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7

    # Database connection URL (SQLAlchemy style or DSN)
    DATABASE_URL: str

    # Tell Pydantic where to load env‐vars from
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"     # ignore any unexpected vars
    )

# Instantiate once for the whole app
settings = Settings()
