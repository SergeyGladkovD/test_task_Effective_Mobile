import json
import os

from book import Book


class Library:
    DATA_FILE = 'library.json'

    def __init__(self):
        self.books = self.load_data()

    @staticmethod
    def load_data():
        """Loads data from JSON file"""
        if not os.path.exists(Library.DATA_FILE):
            return []

        with open(Library.DATA_FILE, 'r') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                print("Ошибка при чтении файла данных.")
                return []

        return [Book.from_dict(book_dict) for book_dict in data]

    def save_data(self):
        """Saves books to JSON file"""
        with open(Library.DATA_FILE, 'w') as f:
            json.dump([book.__dict__ for book in self.books], f, indent=4)

    def add_book(self, title, author, year):
        """Add a book to the library"""
        new_id = len(self.books) + 1
        book = Book(new_id, title, author, year)
        self.books.append(book)
        self.save_data()
        print(f"Книга '{title}' успешно добавлена!")

    def delete_book(self, id_):
        """Delete book with given id."""
        found = False
        for i, book in enumerate(self.books):
            if book.id == id_:
                del self.books[i]
                found = True
                break

        if found:
            self.save_data()
            print(f"Книга с ID {id_} удалена.")
        else:
            print(f"Книга с ID {id_} не найдена.")

    def search_books(self, query=None, field='title'):
        """Search books by query"""
        if query is None or query.strip() == '':
            return self.books

        results = []
        for book in self.books:
            if query.lower() in getattr(book, field).lower():
                results.append(book)

        return results

    def display_all_books(self):
        """Display all books."""
        if not self.books:
            print("Библиотека пуста.")
            return

        print("\nСписок всех книг:")
        for book in self.books:
            print(f"{book.id} | {book.title} | {book.author} | {book.year} | {book.status}")

    def change_status(self, id_, new_status):
        """Change the status of a book."""
        found = False
        for book in self.books:
            if book.id == id_:
                book.status = new_status
                found = True
                break

        if found:
            self.save_data()
            print(f"Статус книги с ID {id_} изменен на '{new_status}'.")
        else:
            print(f"Книга с ID {id_} не найдена.")
