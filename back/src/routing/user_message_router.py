from dependency_injector.containers import DeclarativeContainer
from fastapi import APIRouter, Path

from back.src.schemas.message import Message
from back.src.services.interfaces.IMessageService import IMessageService


def message_router(container: DeclarativeContainer) -> APIRouter:
    router = APIRouter(prefix='/user_message', tags=['user_message'])

    service: IMessageService = container.message_service()

    @router.get("/{message}", response_model=Message)
    async def get_message(
            message: str = Path(..., description="Сообщение от ботика"),
    ) -> Message:

        return await service.get_message(message)

    return router
