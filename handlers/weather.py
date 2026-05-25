from aiogram.types import Message

from aiogram import Router
from aiogram.filters.command import Command
from utils.get_weather import get_weather
from utils.get_weather_1 import get_weather_1
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from keyboards.keyboards import kb1

router = Router()


class WeatherState(StatesGroup):
    waiting_for_city = State()

# weather
@router.message(Command('weather'))
async def weather(message: Message, state:FSMContext):
    await message.answer('Напишите город, покажу погоду!')
    await state.set_state(WeatherState.waiting_for_city)

@router.message(WeatherState.waiting_for_city)
async def weather_handler(message:Message, state: FSMContext):
    city = message.text
    weather_city = await get_weather(city)
    await message.answer(weather_city,
                         reply_markup=kb1)
    await state.clear()





# # weather_1
# @router.message(Command('weather_1'))
# async def weather(message: Message):
#     await message.answer('Напишите город, покажу погоду!')


# @router.message()
# async def weather_handler(message:Message):
#     city = message.text
#     weather_city = await get_weather_1(city)
#     await message.answer(weather_city,
#                          reply_markup=kb1)