import asyncio
import logging
import aiogram
from aiogram import Bot, Dispatcher, types, F
import config
from handlers import weather
from proxy import proxy


async def main():
    TOKEN_TG = config.token_telegram
    TOKEN_OPENAI = config.token_openai
    TOKEN_OPENWEATHER = config.token_openweather

    logging.basicConfig(level=logging.INFO)

    bot = Bot(token=TOKEN_TG, session=proxy())

    dp = Dispatcher()

    dp.include_router(weather.router)

if __name__ == '__main__':
    asyncio.run(main())