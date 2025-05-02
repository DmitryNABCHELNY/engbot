import json
import os

BOOKS_PATH = os.path.join(os.path.dirname(__file__), "books_full.json")

with open(BOOKS_PATH, "r", encoding="utf-8") as f:
    books = json.load(f)

def save_books():
    with open(BOOKS_PATH, "w", encoding="utf-8") as f:
        json.dump(books, f, ensure_ascii=False, indent=2)
