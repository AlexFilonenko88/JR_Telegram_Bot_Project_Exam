from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


btn1 = KeyboardButton(text='/start')
btn2 = KeyboardButton(text='/info')
btn3 = KeyboardButton(text='/weather')

keyboards_1 = [
    [btn1, btn2, btn3]
]

kb1 = ReplyKeyboardMarkup(keyboard=keyboards_1, resize_keyboard=True)