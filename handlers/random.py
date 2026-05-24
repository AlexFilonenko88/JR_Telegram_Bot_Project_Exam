from aiogram.types import Message
from aiogram import F
from aiogram import Router
from aiogram.filters.command import Command

from services.chat_gpt import ChatGptService
from services.facts import get_random_facts

from keyboards.keyboards import kb1, kb2


router = Router()


@router.message(Command("random", "another_fact"))
@router.message(F.text.contains("Рандомный факт"))
async def random_answer(message: Message, chat_gpt_service: ChatGptService):
    await message.answer(f'Ответ random')

    prompt_text = get_random_facts()
    image = await chat_gpt_service.generate_image(prompt_text)

    await message.answer_photo(photo=image,
                               reply_markup=kb2)


@router.message(Command('exit'))
async def another_fact(message: Message):
    await message.answer('Выберите проект:',
                         reply_markup=kb1)
