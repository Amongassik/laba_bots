from aiogram.filters import Command
from aiogram import types,Router

from app.keyboards import main
router = Router()

@router.message(Command("start"))
async def start_cmd(message: types.Message):
    await message.answer('Привет',
                        reply_markup=main
                         )