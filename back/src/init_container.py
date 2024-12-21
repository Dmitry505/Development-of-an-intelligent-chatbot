from dependency_injector import containers, providers
from pathlib import Path

from back.src.utils.VectorStoreService import VectorStoreService
from back.src.utils.LanguageModelService import LanguageModelService
from back.src.services.QuestionAnsweringService import QuestionAnsweringService


def init_container(settings):
    class Container(containers.DeclarativeContainer):
        # Настройки
        config = providers.Configuration()

        # Пути
        current_dir = Path.cwd()
        processed_data_path = providers.Object(
            current_dir.parent / 'data' / 'processed_data' / 'union.parquet'  # Кринж, но хоть работает.
        )

        # Сервисы
        vectorstore_service = providers.Factory(
            VectorStoreService,
            persist_path=processed_data_path,
            embedding_model="llama3.1"
        )

        language_model_service = providers.Factory(
            LanguageModelService,
            model_name="llama3.1",
            temperature=0
        )

        # Основной сервис
        qa_service = providers.Factory(
            QuestionAnsweringService,
            vectorstore_service=vectorstore_service,
            language_model_service=language_model_service
        )

    container = Container()
    container.config.from_dict(settings)

    return container
