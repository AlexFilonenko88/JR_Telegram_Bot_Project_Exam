from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

btn1 = KeyboardButton(text='Начать')
btn2 = KeyboardButton(text='Рандомный факт')
btn3 = KeyboardButton(text='ChatGPT интерфейс')
btn4 = KeyboardButton(text='Диалог с известной личностью')
btn5 = KeyboardButton(text='Погода')
btn7 = KeyboardButton(text='Хочу ещё факт')
btn8 = KeyboardButton(text='Выход')
btn9 = KeyboardButton(text='Квиз')
btn10 = KeyboardButton(text='Переводчик')
btn11 = KeyboardButton(text='Английский')
btn12 = KeyboardButton(text='Немецкий')


keyboards_1 = [
    [btn1],
    [btn2, btn3],
    [btn4, btn5],
    [btn9, btn10]
]
keyboards_2 = [
    [btn7, btn8],
]
keyboards_3 = [
    [btn11, btn12],
]

kb1 = ReplyKeyboardMarkup(keyboard=keyboards_1, resize_keyboard=True)
kb2 = ReplyKeyboardMarkup(keyboard=keyboards_2, resize_keyboard=True)
kb3 = ReplyKeyboardMarkup(keyboard=keyboards_3, resize_keyboard=True)


def personalities_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Альберт Эйнштейн", callback_data="Альберт Эйнштейн")],
        [InlineKeyboardButton(text="Стив Джобс", callback_data="Стив Джобс")],
        [InlineKeyboardButton(text="Фрейд", callback_data="Фрейд")],
    ])


def finish_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Закончить", callback_data="finish")]
    ])


def get_actions_kb():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Сменить язык")],
            [KeyboardButton(text="Закончить")]
        ],
        resize_keyboard=True
    )


QUIZ_TOPICS = ["История", "Наука", "Кино", "География"]


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
