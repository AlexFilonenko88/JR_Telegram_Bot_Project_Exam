import asyncio
import logging
import aiogram
from aiogram import Bot, Dispatcher, types, F
from aiohttp.helpers import TOKEN

import config
from proxy import proxy


async def main():
    TOKEN_TG = config.token_telegram
    TOKEN_OPENAI = config.token_openai

    logging.basicConfig(level=logging.INFO)

    bot = Bot(token=TOKEN_TG, session=proxy())

    dp = Dispatcher()

    # dp.include_router(###.router)

if __name__ == '__main__':
    asyncio.run(main())