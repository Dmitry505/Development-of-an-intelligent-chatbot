import uvicorn
import asyncio
from fastapi import FastAPI
from dependency_injector.containers import DeclarativeContainer
from pydantic_settings import BaseSettings

from back.config import init_settings
from back.src.init_container import init_container
from back.src.routing.user_message_router import message_router


async def fastapi_app(container: DeclarativeContainer, settings: BaseSettings):
    app = FastAPI()

    app.include_router(message_router(container))

    config = uvicorn.Config(
        app,
        reload=True,
        host=settings.run.host,
        port=settings.run.port,)
    server = uvicorn.Server(config=config)

    await server.serve()


if __name__ == '__main__':
    base_settings: BaseSettings = init_settings()
    base_container: DeclarativeContainer = init_container(set)
    asyncio.run(fastapi_app(base_container, base_settings))
