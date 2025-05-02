from aiogram import types, Dispatcher
from data.random_books import get_random_book

async def cmd_random(message: types.Message):
    book = get_random_book()
    await message.answer(
        f"📚 {book['title']} — {book['desc']}\n"
        f"Уровень: {book['level']}, жанр: {book['genre']}"
    )

def register_handlers_random(dp: Dispatcher):
    dp.register_message_handler(cmd_random, commands=["random_book"])

