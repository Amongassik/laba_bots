from aiogram.filters import Command
from aiogram import types,Router,F
from aiogram.fsm.context import FSMContext

from app.keyboards import main,currencies,to_case
from app.parsing.parser import load_currencies,parse
from app.case import CaseHandel,CaseState,get_user_case

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

@router.message(F.text == 'CASE-система')
async def choise_funcs(message:types.Message):
    """Сообщение с функции"""
    await message.answer('Выберете функцию',reply_markup= await to_case(0))

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


@router.callback_query(F.data.startswith("func_"))
async def func_stage(callback:types.CallbackQuery,state:FSMContext):
    calldata = callback.data.split("_")
    stage = int(calldata[1])
    func = calldata[2]

    user_id = callback.from_user.id
    case_= get_user_case(user_id)
    case_.set_func(func,stage)
    if stage == 2:
        await state.set_state(CaseState.for_x)
        await callback.message.edit_text("Введите x")
    else:
        await callback.message.edit_text(f"Записана функция {func}",reply_markup=await to_case(stage+1))
        await callback.answer("Функция выбрана")

@router.message(CaseState.for_x)
async def get_x(message:types.Message,state:FSMContext):
    await state.update_data(for_x =message.text)
    user_id = message.from_user.id
    case_ = get_user_case(user_id)

    data = await state.get_data()
    await message.answer(f"{case_.to_formula()}")
    x = float(data['for_x'])
    case_.set_x(x)
    await state.clear()
    if not case_.check_success():
        await state.set_state(CaseState.for_x)
        await message.answer(f"Введите корректное число.{case_.error}")
    else:
        case_.calculate()
        if case_.check_success():
            await message.answer(f'{case_.message}')
        else:
            await message.answer(f"{case_.error}")





@router.callback_query(F.data == 'close_keyboard')
async def close_keyboard(callback:types.CallbackQuery):
    """Закрыть список"""
    await callback.message.delete()
    await callback.answer()