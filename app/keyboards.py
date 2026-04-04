from aiogram.types import (ReplyKeyboardMarkup,KeyboardButton,
                           InlineKeyboardMarkup,InlineKeyboardButton,)

main = ReplyKeyboardMarkup(
    resize_keyboard=True,
    input_field_placeholder='Выбиерете то что вас интересует',
    one_time_keyboard=True,
    keyboard=[
    [KeyboardButton(text='Курс валют'),KeyboardButton(text='Лаба 11')],]
)