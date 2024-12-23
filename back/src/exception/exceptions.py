import logging
from fastapi import Request
from fastapi.responses import JSONResponse
from src.exception.exception_models.models import VectorStoreError, LanguageModelError


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


async def vector_store_error_handler(request: Request, exc: VectorStoreError):
    logger.error(f"Ошибка в векторном хранилище: {str(exc)}")
    return JSONResponse(
        status_code=500,
        content={"message": f"Ошибка при работе с векторным хранилищем: {str(exc)}"}
    )

async def language_model_error_handler(request: Request, exc: LanguageModelError):
    logger.error(f"Ошибка в языковой модели: {str(exc)}")
    return JSONResponse(
        status_code=500,
        content={"message": f"Ошибка при генерации ответа моделью: {str(exc)}"}
    )

async def general_error_handler(request: Request, exc: Exception):
    logger.error(f"Неизвестная ошибка: {str(exc)}")
    return JSONResponse(
        status_code=500,
        content={"message": "Произошла неизвестная ошибка. Пожалуйста, попробуйте позже."}
    )
