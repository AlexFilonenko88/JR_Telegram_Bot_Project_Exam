from aiogram.types import Message

from aiogram import Router
from aiogram.filters.command import Command, CommandStart
from utils.get_weather import get_weather

from keyboards.keyboards import kb1

router = Router()

@router.message(CommandStart())
async def start(message: Message):
    await message.answer('Выберите проект',
                         reply_markup=kb1)

@router.message(Command('weather'))
async def weather(message: Message):
    await message.answer('Напишите город, покажу погоду!',
                         reply_markup=kb1)

@router.message()
async def weather_handler(message:Message):
    city = message.text
    weather_city = await get_weather(city)
    await message.answer(weather_city)