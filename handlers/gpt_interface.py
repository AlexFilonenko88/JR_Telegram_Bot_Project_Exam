from aiogram.types import Message
from aiogram import Router, F
from aiogram.filters.command import Command
from services.chat_gpt import ChatGptService
import base64
from aiogram.types import BufferedInputFile
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext


router = Router()


class GptState(StatesGroup):
    waiting_for_prompt = State()




@router.message(Command("gpt"))
@router.message(F.text.contains("ChatGPT интерфейс"))
async def cmd_gpt(message: Message, state: FSMContext):
    await message.answer("Напиши, какую картинку сгенерировать 🎨")
    await state.set_state(GptState.waiting_for_prompt)



@router.message(GptState.waiting_for_prompt,
                F.text & ~F.text.startswith("/")
                )
async def generate_image_handler(message: Message, state: FSMContext, chat_gpt_service: ChatGptService):

    prompt = message.text

    image_base64 = await chat_gpt_service.generate_image(prompt)

    if not image_base64:
        await message.answer("Ошибка генерации ❌")
        return

    import base64
    from aiogram.types import BufferedInputFile

    image_bytes = base64.b64decode(image_base64)
    photo = BufferedInputFile(image_bytes, filename="image.png")

    await message.answer_photo(photo=photo)

    await state.clear()