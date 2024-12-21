from pathlib import Path
from langchain_community.vectorstores import SKLearnVectorStore
from langchain_ollama import OllamaEmbeddings
import asyncio
from typing import List

from back.src.exception.exception_models.models import VectorStoreError


class VectorStoreService:
    def __init__(self, persist_path: Path, embedding_model: str):
        self.persist_path = persist_path
        try:
            self.vectorstore = SKLearnVectorStore(
                embedding=OllamaEmbeddings(model=embedding_model),
                persist_path=self.persist_path,
                serializer="parquet"
            )
        except Exception as e:
            raise VectorStoreError(f"Ошибка при инициализации векторного хранилища: {str(e)}")

    async def retrieve_documents(self, question: str, k: int = 3) -> List[str]:
        try:
            retriever = self.vectorstore.as_retriever(k=k)
            return await asyncio.to_thread(retriever.get_relevant_documents, question)
        except Exception as e:
            raise VectorStoreError(f"Ошибка при извлечении документов: {str(e)}")
