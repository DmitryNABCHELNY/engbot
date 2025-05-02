from .view_books import register_view_books
from .add_book import register_add_book
from .delete_book import register_delete_book
from .add_admin import register_add_admin  # Регистрация команды добавления админа

def register_admin(dp):
    register_view_books(dp)
    register_add_book(dp)
    register_delete_book(dp)
    register_add_admin(dp)  # Добавляем команду для регистрации новых админов
