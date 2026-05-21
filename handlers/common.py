from aiogram.types import Message

from aiogram import Router
from aiogram.filters.command import CommandStart

from keyboards.keyboards import kb1

router = Router()


@router.message(CommandStart())
async def start(message: Message):
    await message.answer('Выберите проект:',
                         reply_markup=kb1)


