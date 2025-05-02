from aiogram import types
from data.books import books
from admin.utils import is_admin

async def view_books(message: types.Message):
    if not is_admin(message):
        await message.answer("У вас нет доступа")
        return
    args = message.get_args().split()
    if len(args) < 2:
        await message.answer("Пример: /view_books A1 adventure")
        return

    level = args[0].upper()
    genre = ' '.join(args[1:]).lower()

    if level in books and genre in books[level]:
        reply = f"📚 Книги {level}/{genre}:\n"
        for i, b in enumerate(books[level][genre], 1):
            reply += f"{i}. {b['title']} — {b['desc']}\n"
        await message.answer(reply)
    else:
        await message.answer("Нет книг по заданному уровню и жанру.")

def register_view_books(dp):
    dp.register_message_handler(view_books, commands=["view_books"])
