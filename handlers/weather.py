from aiogram.types import Message

from aiogram import Router
from aiogram.filters.command import Command
from utils.get_weather import get_weather
from utils.get_weather_1 import get_weather_1


router = Router()


# weather
@router.message(Command('weather'))
async def weather(message: Message):
    await message.answer('Напишите город, покажу погоду!')


@router.message()
async def weather_handler(message:Message):
    city = message.text
    weather_city = await get_weather(city)
    await message.answer(weather_city)

# weather_1
@router.message(Command('weather_1'))
async def weather(message: Message):
    await message.answer('Напишите город, покажу погоду!')


@router.message()
async def weather_handler(message:Message):
    city = message.text
    weather_city = await get_weather_1(city)
    await message.answer(weather_city)