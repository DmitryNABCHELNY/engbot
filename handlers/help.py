from aiogram import types, Dispatcher


async def cmd_help(message: types.Message):
    await message.answer(
        "/start — запустить бота\n"
        "/help — инструкция по использованию\n"
        "/recommend <уровень> <жанр> — получить рекомендации\n"
        "/random_book — случайная книга на английском"
    )

def register_handlers_help(dp: Dispatcher):
    dp.register_message_handler(cmd_help, commands=["help"])
