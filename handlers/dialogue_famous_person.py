from aiogram.types import Message
from aiogram import F

from aiogram import Router
from aiogram.filters.command import Command


router = Router()


@router.message(F.text.contains('talk'))
@router.message(F.text.contains("Диалог с известной личностью"))
async def start(message: Message):
    await message.answer('Test')