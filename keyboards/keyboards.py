from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


btn1 = KeyboardButton(text='/start')
btn2 = KeyboardButton(text='/info')
btn3 = KeyboardButton(text='/weather')
btn4 = KeyboardButton(text='/weather_1')

keyboards_1 = [
    [btn1, btn2, btn3, btn4]
]

kb1 = ReplyKeyboardMarkup(keyboard=keyboards_1, resize_keyboard=True)