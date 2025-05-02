from aiogram import types
from data.books import books, save_books
from admin.utils import is_admin

async def add_book(message: types.Message):
    if not is_admin(message):
        await message.answer("У вас нет доступа")
        return
    try:
        _, level, genre, title, desc = message.text.split(";", 4)
        level = level.strip().upper()
        genre = genre.strip().lower()
        title = title.strip()
        desc = desc.strip()

        books.setdefault(level, {}).setdefault(genre, []).append({"title": title, "desc": desc})
        save_books()
        await message.answer("Книга добавлена.")
    except:
        await message.answer("Формат: /add_book; A1; adventure; Название; Описание")

def register_add_book(dp):
    dp.register_message_handler(add_book, lambda m: m.text.startswith("/add_book;"))
