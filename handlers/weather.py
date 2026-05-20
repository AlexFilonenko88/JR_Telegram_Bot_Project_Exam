from aiogram.types import Message

from aiogram import Router, types, F
from aiogram.filters.command import Command

from keyboards.keyboards import kb1

router = Router()

@router.message(Command('weather'))
async def weather(message: Message):
    await message.answer('Hello!',
                         reply_markup=kb1)