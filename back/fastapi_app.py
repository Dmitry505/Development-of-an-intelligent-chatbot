import uvicorn
import asyncio
from fastapi import FastAPI
from dependency_injector.containers import DeclarativeContainer
from pydantic_settings import BaseSettings

from config import init_settings
from src.init_container import init_container
from src.routing.user_message_router import message_router

from src.exception.exception_models.models import VectorStoreError, LanguageModelError
from src.exception.exceptions import vector_store_error_handler, language_model_error_handler, general_error_handler
from fastapi.middleware.cors import CORSMiddleware


async def fastapi_app(container: DeclarativeContainer, settings: BaseSettings):
    app = FastAPI()
    app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"], 
)
    app.include_router(message_router(container))

    app.add_exception_handler(LanguageModelError, language_model_error_handler)
    app.add_exception_handler(VectorStoreError, vector_store_error_handler)
    app.add_exception_handler(Exception, general_error_handler)

    config = uvicorn.Config(
        app,
        reload=True,
        host=settings.run.host,
        port=settings.run.port,)
    server = uvicorn.Server(config=config)

    await server.serve()


if __name__ == '__main__':
    base_settings: BaseSettings = init_settings()
    base_container: DeclarativeContainer = init_container(settings=base_settings)
    asyncio.run(fastapi_app(base_container, base_settings))
