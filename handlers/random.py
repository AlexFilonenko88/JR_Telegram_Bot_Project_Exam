from aiogram.types import Message

from aiogram import Router
from aiogram.filters.command import Command
from services.chat_gpt import ChatGptService
from services.facts import get_random_facts
from keyboards.keyboards import kb1

router = Router()

# @router.message(Command('random'))
# async def start(message: Message):
#     await message.answer('Test:')


@router.message(Command('random'))
async def random_answer(message: Message, chat_gpt_service: ChatGptService):
    await message.answer(f'Ответ')
    # role_text = '''
    #             Факт
    #             '''
    # answer = await chat_gpt_service.ask(
    #     user_text = message.text,
    #     role_text = role_text,
    # )
    #
    # await message.answer(f'Ответ {answer}')

    prompt_text = get_random_facts()
    image = await chat_gpt_service.generate_image(prompt_text)

    await message.answer_photo(photo=image)