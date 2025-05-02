import json
import os
from aiogram.types import Message

ADMINS_FILE = os.path.join(os.path.dirname(__file__), "../data/admins.json")

def load_admins():
    """Загружает список админов из файла JSON."""
    with open(ADMINS_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data.get("admins", [])

def save_admins(admins):
    """Сохраняет обновленный список админов в файл JSON."""
    with open(ADMINS_FILE, "w", encoding="utf-8") as f:
        json.dump({"admins": admins}, f, ensure_ascii=False, indent=2)

def is_admin(message: Message):
    """Проверяет, является ли пользователь админом."""
    admins = load_admins()
    return message.from_user.username in admins

def add_admin(username: str):
    """Добавляет нового админа в список и сохраняет его в файл."""
    admins = load_admins()
    if username not in admins:
        admins.append(username)
        save_admins(admins)
        return True
    return False
