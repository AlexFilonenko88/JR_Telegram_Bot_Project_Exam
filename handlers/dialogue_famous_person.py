from aiogram.types import Message, CallbackQuery
from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram import Router
from services.chat_gpt import ChatGptService
from aiogram.filters.command import Command
from keyboards.keyboards import personalities_keyboard, finish_keyboard
import base64
from aiogram.types import BufferedInputFile
from data.personal_prompts import PERSON_PROMPTS


router = Router()


class TalkState(StatesGroup):
    choosing = State()
    talking = State()

@router.message(Command('talk'))
@router.message(F.text & F.text.contains("Диалог с известной личностью"))
async def talk_person(message: Message, state: FSMContext, chat_gpt_service: ChatGptService):
    await state.set_state(TalkState.choosing)

    # prompt_text = 'Einstein'
    # image_person = await chat_gpt_service.generate_image(prompt_text)

    await message.answer(
        text="Выбери личность, с которой хочешь поговорить:",
        reply_markup=personalities_keyboard()
    )

@router.callback_query(F.data.in_(PERSON_PROMPTS.keys()))
async def choose_personality(callback: CallbackQuery, state: FSMContext, chat_gpt_service: ChatGptService):
    personality = callback.data
    await state.update_data(prompt=PERSON_PROMPTS[personality])
    await state.set_state(TalkState.talking)

    image_person_base64 = await chat_gpt_service.generate_image(callback.data)

    if not image_person_base64:
        await message.answer("Ошибка: картинка не найдена ❌")
        return

    image_bytes = base64.b64decode(image_person_base64)

    image_person = BufferedInputFile(image_bytes, filename="image.png")

    await callback.message.answer_photo(
        image_person
    )

    await callback.message.answer(
        f"Отлично! Теперь ты разговариваешь с *{callback.data}*.\nПиши сообщение.",
        parse_mode="Markdown",
        reply_markup=finish_keyboard()
    )
    await callback.answer()



@router.message(TalkState.talking)
async def talk_with_person(message: Message, state: FSMContext, chat_gpt_service: ChatGptService):
    data = await state.get_data()
    prompt = data.get("prompt")

    if not prompt:
        await message.answer("Ошибка: личность не выбрана. Используй /talk чтобы начать.")
        return


    answer = await chat_gpt_service.ask(
        user_text=message.text,
        role_text=prompt
    )

    await message.answer(answer,
                        reply_markup=finish_keyboard()
                        )



@router.callback_query(F.data == "finish")
async def finish(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.message.answer("Диалог завершён. Используй /talk чтобы начать снова.")
    await callback.answer()