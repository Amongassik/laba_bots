from aiogram.types import (ReplyKeyboardMarkup,KeyboardButton,
                           InlineKeyboardMarkup,InlineKeyboardButton,)
from aiogram.utils.keyboard import ReplyKeyboardBuilder,InlineKeyboardBuilder
from app.parsing.parser import load_currencies
#Главная клавиатура выбора
main = ReplyKeyboardMarkup(
    resize_keyboard=True,
    input_field_placeholder='Выбиерете то что вас интересует',
    one_time_keyboard=True,
    keyboard=[
    [KeyboardButton(text='Курс валют'),KeyboardButton(text='Лаба 11')],]
)

action_one = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text='Обновить',callback_data='update_cur'),
        InlineKeyboardButton(text='Закрыть',callback_data='close_keyboard')
    ]]
)

async def currencies():
    """
    Генерация клавиатуры для выбора валют
        должен получать не в параметрах а внутри себя список валют и создавать кнопки
    """
    keyboard = InlineKeyboardBuilder()

    data = load_currencies()

    if not data:
        keyboard.add(InlineKeyboardButton(
            text='Нет данных',
            callback_data="update_cur"
        ))
        return keyboard.as_markup()
    
    for cur in data:
        id = cur.get('id')
        name = cur.get('name')
        rate = cur.get('sum')

        text = name.replace('/RUB', '').replace(' F', '').strip()

        keyboard.add(
            InlineKeyboardButton(
                text=text,
                callback_data=f"cur_{id}",
            )
        )
    
    keyboard.adjust(3)
    keyboard.row(
        InlineKeyboardButton(text='Обновить',callback_data="update_cur")
    )

    keyboard.row(
        InlineKeyboardButton(text="Закрыть", callback_data="close_keyboard")
    )
    return keyboard.as_markup()
        