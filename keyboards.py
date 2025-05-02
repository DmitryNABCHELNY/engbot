from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_main_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton(text="🔍 Найти книгу", callback_data="find_book"),
        InlineKeyboardButton(text="🎲 Случайная книга", callback_data="random_book"),
        InlineKeyboardButton(text="ℹ️ Помощь", callback_data="help")
    )
    return keyboard
