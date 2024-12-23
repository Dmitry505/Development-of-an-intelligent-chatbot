import requests
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command
from dotenv import load_dotenv
import os

# Тут реализация использования бота вместо сайта, работает от запущенного fastapi

load_dotenv()

# Укажите ваш токен Telegram-бота
TELEGRAM_TOKEN = os.getenv("BOT_TOKEN")

# Укажите URL вашего FastAPI сервера
FASTAPI_URL = "http://localhost:8000/user_message/{message}"  # Замените на ваш URL FastAPI

# Инициализация бота и диспетчера
bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher()

@dp.message(Command(commands=["start", "help"]))
async def cmd_start(message: Message):
    await message.reply("Привет! Отправь мне сообщение, и я отвечу!")

@dp.message()
async def send_to_fastapi(message: Message):
    try:
        # Отправляем текст на сервер FastAPI
        response = requests.get(FASTAPI_URL.format(message=message.text))
        response.raise_for_status()
        result = response.json()  # Предполагаем, что API возвращает JSON

        print(message)
        print(result)

        # Отправляем результат обратно пользователю
        await message.answer(result.get("text", "Ответ не получен"))
    except requests.RequestException as e:
        await message.answer(f"Ошибка при обращении к API: {e}")
    except Exception as e:
        await message.answer(f"Произошла ошибка: {e}")

async def main():
    print("Бот запущен")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())