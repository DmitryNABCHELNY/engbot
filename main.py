from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from config import API_TOKEN
from keyboards import get_main_keyboard
from handlers import start, help, recommend,inline_book_random, random_book
from admin import register_admin

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Регистрируем хендлеры
inline_book_random.register_handlers_random_inline(dp)
start.register_handlers_start(dp)
help.register_handlers_help(dp)
recommend.register_handlers_recommend(dp)
random_book.register_handlers_random(dp)
register_admin(dp)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
