from aiogram.types import Message

from aiogram import Router
from aiogram.filters.command import Command


router = Router()


@router.message(Command('info'))
async def random_answer(message: Message):
    await message.answer(f'Ответ info')
