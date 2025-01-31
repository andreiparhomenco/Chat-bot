import os
import dotenv
import asyncio
import logging
from aiogram.types import Message
from aiogram import BaseMiddleware

from aiogram import Bot, Dispatcher

from app.handlers import router

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("bot.log"),
        logging.StreamHandler()
    ]
)


dotenv.load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher()

class LoggingMiddleware(BaseMiddleware):
    async def __call__(self, handler, event: Message, data):
        first_name = event.from_user.first_name
        last_name = event.from_user.last_name or ""
        username = event.from_user.username or "No username"
        user_name = f"{first_name} {last_name}".strip()

        logging.info(
            f"Received message from user ({user_name}, @{username}): {event.text}"
        )
        return await handler(event, data)

dp.message.middleware(LoggingMiddleware())



async def main():
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    # logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")
