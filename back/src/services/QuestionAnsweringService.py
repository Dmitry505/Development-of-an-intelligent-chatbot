from src.utils.VectorStoreService import VectorStoreService
from src.utils.LanguageModelService import LanguageModelService

from src.services.interfaces.IModelService import IModelService

from src.exception.exception_models.models import LanguageModelError, VectorStoreError

from src.schemas.message import Message


class QuestionAnsweringService(IModelService):
    def __init__(self, vectorstore_service: VectorStoreService, language_model_service: LanguageModelService):
        self.vectorstore_service = vectorstore_service
        self.language_model_service = language_model_service

    async def get_answer(self, question: str) -> Message:
        try:
            documents = await self.vectorstore_service.retrieve_documents(question)
            result = await self.language_model_service.get_response(question, documents)
            return Message(text=result)
        except (VectorStoreError, LanguageModelError) as e:
            raise e
        except Exception as e:
            raise Exception(f"Общая ошибка при обработке запроса: {str(e)}")
