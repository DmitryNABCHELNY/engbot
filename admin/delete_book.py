from aiogram import types
from data.books import books, save_books
from admin.utils import is_admin

async def delete_book(message: types.Message):
    if not is_admin(message):
        await message.answer("У вас нет доступа")
        return
    args = message.get_args().split()
    if len(args) < 3:
        await message.answer("Пример: /delete_book A1 adventure 2")
        return

    level, genre, idx = args[0].upper(), args[1].lower(), int(args[2]) - 1

    if level in books and genre in books[level] and 0 <= idx < len(books[level][genre]):
        deleted = books[level][genre].pop(idx)
        save_books()
        await message.answer(f"Удалено: {deleted['title']}")
    else:
        await message.answer("Неверные данные.")

def register_delete_book(dp):
    dp.register_message_handler(delete_book, commands=["delete_book"])
