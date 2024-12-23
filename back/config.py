import os
from pydantic_settings import BaseSettings
from pydantic import BaseModel
from dotenv import load_dotenv


load_dotenv()


class RunConfig(BaseModel):
    host: str = "127.0.0.1"
    port: int = 8000


class Settings(BaseSettings):
    run: RunConfig = RunConfig()


def init_settings():
    return Settings()
