from abc import ABC, abstractmethod

from back.src.schemas.message import Message


class IMessageService(ABC):
    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    async def get_message(self, message: str) -> Message:
        raise NotImplementedError()
