import pytest
from httpx import AsyncClient
import asyncio
import time

BASE_URL = "http://127.0.0.1:8000"


@pytest.mark.asyncio
async def test_parallel_requests():
    messages = [f"Базы данных {i}" for i in range(5)]  # Список сообщений
    async with AsyncClient(base_url=BASE_URL, timeout=60) as client:
        # Формируем задачи для параллельных запросов с замером времени
        tasks = []

        # Создаем задачи для каждого запроса
        for msg in messages:
            tasks.append(
                asyncio.create_task(
                    make_request(client, msg)
                )
            )

        # Выполняем все запросы параллельно
        await asyncio.gather(*tasks)


async def make_request(client, msg):
    start_time = time.time()  # Засекаем время перед запросом
    response = await client.get(f"/user_message/{msg}")
    elapsed_time = time.time() - start_time  # Вычисляем время ответа

    # Выводим время ответа для каждого запроса
    print(f"\nВремя ответа для запроса '{msg}': {elapsed_time:.2f} секунд")

    # Проверяем, что статус код ответа 200
    assert response.status_code == 200
    data = response.json()

    # Проверяем, что в ответе есть поле 'text'
    assert "text" in data

    # Проверяем, что текст не совпадает с исходным сообщением
    assert data["text"] != msg, f"Ответ для '{msg}' не является случайным"
