import asyncio
import logging
import aiogram
from aiogram import Bot, Dispatcher
import config
from handlers import weather, common, random, gpt_interface, dialogue_famous_person, translator, quiz
from proxy import proxy
from services.chat_gpt import ChatGptService



async def main():
    TOKEN_TG = config.token_telegram
    TOKEN_OPENAI = config.token_openai

    logging.basicConfig(level=logging.INFO)

    # bot = Bot(token=TOKEN_TG, session=proxy())
    bot = Bot(token=TOKEN_TG)

    dp = Dispatcher()

    chat_gpt_service = ChatGptService(api_key=TOKEN_OPENAI)
    dp['chat_gpt_service'] = chat_gpt_service


    dp.include_router(common.router)
    dp.include_router(random.router)
    dp.include_router(gpt_interface.router)
    dp.include_router(dialogue_famous_person.router)
    dp.include_router(translator.router)
    dp.include_router(weather.router)
    dp.include_router(quiz.router)


    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())