from aiogram.types import Message
from aiogram import F
from aiogram import Router
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from services.chat_gpt import ChatGptService
from aiogram.fsm.state import StatesGroup, State
from keyboards.keyboards import kb1, kb3, get_actions_kb


router = Router()


class TranslatorState(StatesGroup):
    choosing_language = State()
    waiting_text = State()


@router.message(Command("translator"))
@router.message(F.text == "Переводчик")
async def start_translator(message: Message, state: FSMContext):
    await state.set_state(TranslatorState.choosing_language)
    await message.answer(
        "Выберите язык:",
        reply_markup=kb3
    )

@router.message(TranslatorState.choosing_language)
async def choose_language(message: Message, state: FSMContext):
    lang = message.text

    await state.update_data(lang=lang)
    await state.set_state(TranslatorState.waiting_text)

    await message.answer(
        f"Вы выбрали: {lang}\nТеперь отправьте текст"
    )


@router.message(TranslatorState.waiting_text, F.text == "Сменить язык")
async def change_language(message: Message, state: FSMContext):
    await state.set_state(TranslatorState.choosing_language)
    await message.answer("Выберите новый язык:",
                        reply_markup=kb3)



@router.message(TranslatorState.waiting_text, F.text == "Закончить")
async def stop_translator(message: Message, state: FSMContext):
    await state.clear()
    await message.answer('Выберите проект:',
                         reply_markup=kb1)



@router.message(TranslatorState.waiting_text)
async def translate_text(message: Message, state: FSMContext, chat_gpt_service: ChatGptService):
    data = await state.get_data()
    lang = data.get("lang")

    user_text = message.text

    prompt = f"Переведи на {lang}: {user_text}"

    result = await chat_gpt_service.ask(prompt,
                                        f"Ты профессиональный переводчик. Переводи на {lang}.")

    await message.answer(
        result,
        reply_markup=get_actions_kb()
    )
