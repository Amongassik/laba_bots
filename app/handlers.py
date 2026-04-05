from aiogram.filters import Command
from aiogram import types,Router,F

from app.keyboards import main,currencies
from app.parsing.parser import load_currencies,parse
router = Router()

@router.message(Command("start"))
async def start_cmd(message: types.Message):
    """Приветсвие с выбором лабораторной"""
    await message.answer('Привет',
                        reply_markup=main
                         )

@router.message(F.text == 'Курс валют')
async def choise_currencies(message:types.Message):
    """Сообщение с выбором валюты"""
    await message.answer('Выберете валюту',reply_markup= await currencies())

@router.callback_query(F.data.startswith("cur_"))
async def show_cur_rate(callback:types.CallbackQuery):
    """Обработчки каждой валюты"""
    cur_id=callback.data.replace("cur_","")
    data = load_currencies()

    selected_cur = None

    selected_cur = next(
        (cur for cur in data if str(cur.get('id')) == cur_id),
        None
    )

    if selected_cur:
        name = selected_cur.get('name')
        rate = selected_cur.get('sum')

        await callback.message.edit_text(
            f"<b>{name}</b>\n"
            f"Курс: <code>{rate} ₽</code>",
            parse_mode='HTML'
        )
    else:
        await callback.answer("Нет данных", show_alert=True)
    await callback.answer()

@router.callback_query(F.data == "update_cur")
async def update_cur(callback:types.CallbackQuery):
    """Обновление валют"""
    parse()
    await callback.answer("Курсы обновлены",show_alert=True)

@router.callback_query(F.data == 'close_keyboard')
async def close_keyboard(callback:types.CallbackQuery):
    """Закрыть список валют"""
    await callback.message.delete()
    await callback.answer()