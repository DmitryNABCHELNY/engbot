import json
import os
import random

# Путь к файлу books_full.json
BOOKS_FILE = os.path.join(os.path.dirname(__file__), "books_full.json")

# Загрузка данных
with open(BOOKS_FILE, "r", encoding="utf-8") as f:
    books_full = json.load(f)

# Преобразуем данные в список книг с указанием уровня и жанра
all_books = []
for level, genres in books_full.items():
    for genre, books in genres.items():
        for book in books:
            all_books.append({
                "title": book["title"],
                "desc": book["desc"],
                "level": level,
                "genre": genre
            })

def get_random_book():
    return random.choice(all_books)
