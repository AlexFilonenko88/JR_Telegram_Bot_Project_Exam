from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


btn1 = KeyboardButton(text='/start')
btn2 = KeyboardButton(text='/random') # /random
btn3 = KeyboardButton(text='/info')
btn4 = KeyboardButton(text='/weather')
btn5 = KeyboardButton(text='/weather_1')

keyboards_1 = [
    [btn1, btn2, btn3],
    [btn4, btn5]
]

kb1 = ReplyKeyboardMarkup(keyboard=keyboards_1, resize_keyboard=True)