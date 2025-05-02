from aiogram import types, Dispatcher
from data.books import books

async def cmd_recommend(message: types.Message):
    args = message.get_args().split()
    if len(args) < 2:
        await message.answer("Пожалуйста, укажи уровень языка и жанр, например: /recommend A1 classic")
        return

    level = args[0].upper()
    genre = ' '.join(args[1:]).lower()

    if level in books and genre in books[level]:
        recs = books[level][genre]
        response = f"Вот несколько книг уровня {level} в жанре {genre}:\n\n"
        for b in recs:
            response += f"📖 {b['title']} — {b['desc']}\n"
        await message.answer(response)
    else:
        await message.answer("Извините, я не нашёл книги по этим критериям. Попробуйте другой уровень или жанр.")

def register_handlers_recommend(dp: Dispatcher):
    dp.register_message_handler(cmd_recommend, commands=["recommend"])
