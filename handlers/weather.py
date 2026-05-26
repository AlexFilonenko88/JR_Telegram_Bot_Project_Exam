from aiogram.types import Message
from aiogram import Router, F
from aiogram.filters.command import Command
from utils.get_weather import get_weather
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from keyboards.keyboards import kb1

router = Router()


class WeatherState(StatesGroup):
    waiting_for_city = State()


@router.message(Command('weather'))
@router.message(F.text.contains("Погода"))
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
