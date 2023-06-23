from pydantic import BaseSettings


class Settings(BaseSettings):
    confirmation_url: str

    class Config:
        env_prefix = ''
        env_file = "app/.env"
        env_file_encoding = "utf-8"


settings = Settings()
