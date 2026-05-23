from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


btn1 = KeyboardButton(text='/start')
# btn2 = KeyboardButton(text='random')
btn2 = KeyboardButton(text='Рандомный факт')
# btn2 = KeyboardButton(text='random_1')
btn3 = KeyboardButton(text='/info')
btn4 = KeyboardButton(text='/weather')
btn5 = KeyboardButton(text='/weather_1')
btn6 = KeyboardButton(text='/another_fact')
btn7 = KeyboardButton(text='/exit')


keyboards_1 = [
    [btn1, btn2, btn3],
    [btn4, btn5]
]
keyboards_2 = [
    [btn6, btn7],
]

kb1 = ReplyKeyboardMarkup(keyboard=keyboards_1, resize_keyboard=True)
kb2 = ReplyKeyboardMarkup(keyboard=keyboards_2, resize_keyboard=True)

