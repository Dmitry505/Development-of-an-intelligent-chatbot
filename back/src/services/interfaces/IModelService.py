from abc import ABC, abstractmethod

from back.src.schemas.message import Message


class IModelService(ABC):
    @abstractmethod
    async def get_answer(self, question: str) -> Message:
        raise NotImplementedError()
