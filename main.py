from library import Library


def main_menu():
    """Main menu"""
    library = Library()

    while True:
        print("\nМеню управления библиотекой:")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Искать книгу")
        print("4. Просмотреть все книги")
        print("5. Изменить статус книги")
        print("0. Выход")

        choice = input("Введите номер команды: ")

        if choice == '1':
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = input("Введите год издания: ")

            library.add_book(title, author, year)

        elif choice == '2':
            id_ = int(input("Введите ID книги для удаления: "))
            library.delete_book(id_)

        elif choice == '3':
            query = input("Введите запрос для поиска (оставьте пустым для просмотра всех книг): ")
            field = input("По какому полю искать? (title/author/year): ")
            results = library.search_books(query, field)

            if results:
                print("\nРезультаты поиска:")
                for book in results:
                    print(f"{book.id} | {book.title} | {book.author} | {book.year} | {book.status}")
            else:
                print("Книги не найдены.")

        elif choice == '4':
            library.display_all_books()

        elif choice == '5':
            id_ = int(input("Введите ID книги для изменения статуса: "))
            new_status = input("Введите новый статус ('в наличии' или 'выдана'): ")
            library.change_status(id_, new_status)

        elif choice == '0':
            print("Завершение работы программы.")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main_menu()
