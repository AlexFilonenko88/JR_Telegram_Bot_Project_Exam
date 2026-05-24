from aiogram.types import Message
from aiogram import F
from aiogram import Router
from aiogram.filters.command import Command
from services.chat_gpt import ChatGptService

router = Router()


@router.message(Command("gpt"))
@router.message(F.text.contains("ChatGPT интерфейс"))
async def random_answer(message: Message, chat_gpt_service: ChatGptService):
    await message.answer('Ответ gpt интерфейс')
    image = await chat_gpt_service.generate_image(message.text)

    await message.answer_photo(photo=image)


