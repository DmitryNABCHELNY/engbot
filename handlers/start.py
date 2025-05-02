from aiogram import types, Dispatcher
from keyboards import *

async def cmd_start(message: types.Message):
    await message.answer(
        "Привет! Я помогу тебе найти интересные книги на английском языке. "
        "Используй следующие команды:\n/help, /recommend, /random_book", reply_markup=get_main_keyboard())

def register_handlers_start(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands=["start"])
