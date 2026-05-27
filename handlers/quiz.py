from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

from services.chat_gpt import ChatGptService

router = Router()

# -----------------------------
# Хранилище состояния
# -----------------------------
user_quiz_state = {}

QUIZ_TOPICS = ["История", "Наука", "Кино", "География"]


# -----------------------------
# Клавиатуры
# -----------------------------
def topics_keyboard():
    kb = InlineKeyboardBuilder()
    for topic in QUIZ_TOPICS:
        kb.button(text=topic, callback_data=f"quiz_topic:{topic}")
    return kb.as_markup()


def after_answer_keyboard():
    kb = InlineKeyboardBuilder()
    kb.button(text="Ещё вопрос", callback_data="quiz_next")
    kb.button(text="Сменить тему", callback_data="quiz_change")
    kb.button(text="Закончить", callback_data="quiz_stop")
    return kb.as_markup()


# -----------------------------
# /quiz
# -----------------------------
@router.message(Command("quiz"))
@router.message(F.text.contains("Квиз"))
async def quiz_start(message: Message):
    photo = FSInputFile("images/quiz.png")

    await message.answer_photo(
        photo,
        caption="🎯 Добро пожаловать в квиз!"
    )

    await message.answer(
        "Выбери тему:",
        reply_markup=topics_keyboard()
    )


# -----------------------------
# Выбор темы
# -----------------------------
@router.callback_query(F.data.startswith("quiz_topic:"))
async def quiz_choose_topic(callback: CallbackQuery, chat_gpt_service: ChatGptService):
    topic = callback.data.split(":")[1]

    user_quiz_state[callback.from_user.id] = {
        "topic": topic,
        "score": 0,
        "question": None
    }

    # Генерация вопроса
    question = await chat_gpt_service.ask(
        user_text=f"Сгенерируй один вопрос квиза по теме '{topic}'. Только вопрос.",
        role_text="Ты генератор вопросов для квиза."
    )

    user_quiz_state[callback.from_user.id]["question"] = question

    await callback.message.answer(
        f"📚 Тема: {topic}\n\n❓ Вопрос:\n{question}\n\nНапиши ответ текстом 👇"
    )

    await callback.answer()


# -----------------------------
# Ответ пользователя
# -----------------------------
@router.message(F.text & ~F.text.startswith("/"))
async def quiz_answer(message: Message, chat_gpt_service: ChatGptService):
    user_id = message.from_user.id

    # Если не в квизе — игнор
    if user_id not in user_quiz_state:
        return

    state = user_quiz_state[user_id]

    # Нет активного вопроса
    if not state["question"]:
        return

    user_answer = message.text
    question = state["question"]
    topic = state["topic"]

    # Проверка ответа
    result = await chat_gpt_service.ask(
        user_text=(
            f"Тема: {topic}\n"
            f"Вопрос: {question}\n"
            f"Ответ пользователя: {user_answer}\n\n"
            f"Ответь строго в формате:\n"
            f"correct: yes/no\n"
            f"explanation: ..."
        ),
        role_text="Ты проверяешь ответы квиза."
    )

    # Подсчёт очков
    if "correct: yes" in result.lower():
        state["score"] += 1

    score = state["score"]

    await message.answer(
        f"{result}\n\n🏆 Счёт: {score}",
        reply_markup=after_answer_keyboard()
    )

    # сбрасываем вопрос
    state["question"] = None


# -----------------------------
# Следующий вопрос
# -----------------------------
@router.callback_query(F.data == "quiz_next")
async def quiz_next(callback: CallbackQuery, chat_gpt_service: ChatGptService):
    user_id = callback.from_user.id
    state = user_quiz_state.get(user_id)

    if not state:
        await callback.answer("Квиз уже завершён", show_alert=True)
        return

    topic = state["topic"]

    question = await chat_gpt_service.ask(
        user_text=f"Сгенерируй новый вопрос квиза по теме '{topic}'. Только вопрос.",
        role_text="Ты генератор вопросов."
    )

    state["question"] = question

    await callback.message.answer(
        f"❓ Новый вопрос ({topic}):\n\n{question}"
    )

    await callback.answer()


# -----------------------------
# Смена темы
# -----------------------------
@router.callback_query(F.data == "quiz_change")
async def quiz_change(callback: CallbackQuery):
    await callback.message.answer(
        "Выбери новую тему:",
        reply_markup=topics_keyboard()
    )
    await callback.answer()


# -----------------------------
# Завершение квиза
# -----------------------------
@router.callback_query(F.data == "quiz_stop")
async def quiz_stop(callback: CallbackQuery):
    user_id = callback.from_user.id

    score = user_quiz_state.get(user_id, {}).get("score", 0)

    await callback.message.answer(
        f"🏁 Квиз завершён!\nТвой результат: {score}"
    )

    user_quiz_state.pop(user_id, None)

    await callback.answer()