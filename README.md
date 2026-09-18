# Sprint_4

Юнит-тесты класса BooksCollector.

- `test_add_new_book_add_two_books` - в словарь попадают две книги
- `test_add_new_book_name_length` - имя 1 и 40 символов добавляется, пустое и 41 символ нет
- `test_set_book_genre_existing_book_genre_is_set` - существующей книге ставится каждый жанр из списка
- `test_get_book_genre_returns_assigned_genre` - по имени возвращается установленный жанр
- `test_get_books_with_specific_genre_returns_matching_books` - в списке только книги нужного жанра
- `test_get_books_genre_returns_current_dictionary` - возвращается текущий словарь книг
- `test_get_books_for_children_filters_age_rating` - детям подходят фантастика, мультфильмы и комедии, ужасы и детективы нет
- `test_add_book_in_favorites_adds_book_only_once` - книга из словаря попадает в избранное один раз
- `test_delete_book_from_favorites_removes_book` - книга удаляется из избранного
- `test_get_list_of_favorites_books_returns_added_books` - возвращается список избранных книг
