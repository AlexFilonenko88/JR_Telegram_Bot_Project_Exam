from aiogram.types import Message, CallbackQuery
from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram import Router
from services.chat_gpt import ChatGptService
from aiogram.filters.command import Command
from keyboards.keyboards import personalities_keyboard, finish_keyboard
from data.personal_prompts import PERSON_PROMPTS


router = Router()


class TalkState(StatesGroup):
    choosing = State()
    talking = State()

@router.message(Command('talk'))
@router.message(F.text & F.text.contains("Диалог с известной личностью"))
async def talk_person(message: Message, state: FSMContext, chat_gpt_service: ChatGptService):
    await state.set_state(TalkState.choosing)

    prompt_text = 'Einstein'
    image_person = await chat_gpt_service.generate_image(prompt_text)

    await message.answer_photo(
        image_person,
        caption="Выбери личность, с которой хочешь поговорить:",
        reply_markup=personalities_keyboard()
    )

@router.callback_query(F.data.in_(PERSON_PROMPTS.keys()))
async def choose_personality(callback: CallbackQuery, state: FSMContext):
    personality = callback.data
    await state.update_data(prompt=PERSON_PROMPTS[personality])
    await state.set_state(TalkState.talking)

    await callback.message.answer(
        f"Отлично! Теперь ты разговариваешь с *{callback.data}*.\nПиши сообщение.",
        parse_mode="Markdown",
        reply_markup=finish_keyboard()
    )
    await callback.answer()


@router.callback_query(F.data == "finish")
async def finish(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.message.answer("Диалог завершён. Используй /talk чтобы начать снова.")
    await callback.answer()