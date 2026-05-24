from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


btn1 = KeyboardButton(text='/start')
btn2 = KeyboardButton(text='Рандомный факт')
btn3 = KeyboardButton(text='ChatGPT интерфейс')
btn4 = KeyboardButton(text='Диалог с известной личностью')
btn5 = KeyboardButton(text='/weather')
btn6 = KeyboardButton(text='/weather_1')
btn7 = KeyboardButton(text='/another_fact')
btn8 = KeyboardButton(text='/exit')



keyboards_1 = [
    [btn1, btn2, btn3],
    [btn4, btn5]
]
keyboards_2 = [
    [btn7, btn8],
]

kb1 = ReplyKeyboardMarkup(keyboard=keyboards_1, resize_keyboard=True)
kb2 = ReplyKeyboardMarkup(keyboard=keyboards_2, resize_keyboard=True)

