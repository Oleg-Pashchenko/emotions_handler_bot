from aiogram import Bot

from bot import dp
from aiogram.enums import ParseMode
import asyncio
from os import getenv
import dotenv

dotenv.load_dotenv()
TOKEN = getenv("TELEGRAM_TOKEN")
bot = Bot(TOKEN, parse_mode=ParseMode.HTML)


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
