from aiogram import types
from admin.utils import is_admin, add_admin


async def add_admin_command(message: types.Message):
    if not is_admin(message):
        await message.answer("У вас нет доступа для добавления новых админов.")
        return

    # Получаем username нового админа
    args = message.get_args().strip()
    if not args:
        await message.answer("Пожалуйста, укажите username для добавления в список админов.")
        return

    if add_admin(args):
        await message.answer(f"Админ {args} был успешно добавлен.")
    else:
        await message.answer(f"Админ {args} уже есть в списке.")

def register_add_admin(dp):
    dp.register_message_handler(add_admin_command, commands=["add_admin"])
