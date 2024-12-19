from back.src.schemas.message import Message
from back.src.services.interfaces.IMessageService import IMessageService


class MessageService(IMessageService):
    def __init__(self) -> None:
        pass

    async def get_message(self, message: str )-> Message:
        return Message(text=message)   # сюда поместить функцию с ботом и переделайте ее по возможности под асинхронную
