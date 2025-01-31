from pydantic_settings import BaseSettings
from pydantic import SecretStr

class Settings(BaseSettings):
    secret_key: SecretStr
    debug: bool
    allowed_hosts: list[str]
    csrf_trusted_origins: list[str]

    class Config:
        env_file = ".env"

settings = Settings()