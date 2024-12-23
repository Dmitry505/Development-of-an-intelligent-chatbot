import asyncio
from typing import List
from langchain_ollama import ChatOllama
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from src.exception.exception_models.models import LanguageModelError


class LanguageModelService:
    def __init__(self, model_name: str, temperature: float = 0):
        try:
            self.llm = ChatOllama(model=model_name, temperature=temperature)
            self.prompt_template = PromptTemplate(
                template="""Вы помощник в вопросах-ответах.
                Для ответа на вопрос используйте следующие документы если они полезны.
                Если вы не знаете ответа, поробуйте ответить самостоятельно или просто скажите, что не знаете.
                Вопрос {question}
                Документы: {documents}
                Отвечать:
                """,
                input_variables=["question", "documents"],
            )
            self.chain = self.prompt_template | self.llm | StrOutputParser()
        except Exception as e:
            raise LanguageModelError(f"Ошибка при инициализации языковой модели: {str(e)}")

    async def get_response(self, question: str, documents: List[str]) -> str:
        try:
            return await asyncio.to_thread(self.chain.invoke, {"question": question, "documents": documents})
        except Exception as e:
            raise LanguageModelError(f"Ошибка при обработке запроса в языковой модели: {str(e)}")
