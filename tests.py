from main import BooksCollector
import pytest


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_genre, который нам возвращает метод get_books_genre, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    @pytest.mark.parametrize(
        'name, book_added',
        [
            ['A', True],
            ['A' * 40, True],
            ['', False],
            ['A' * 41, False],
        ]
    )
    def test_add_new_book_name_length(self, name, book_added):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert (name in collector.get_books_genre()) is book_added

    @pytest.mark.parametrize(
        'genre',
        ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
    )
    def test_set_book_genre_existing_book_genre_is_set(self, genre):
        collector = BooksCollector()
        collector.add_new_book('Ревизор')
        collector.set_book_genre('Ревизор', genre)
        assert collector.get_book_genre('Ревизор') == genre

    def test_get_book_genre_returns_assigned_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Вий')
        collector.set_book_genre('Вий', 'Ужасы')
        assert collector.get_book_genre('Вий') == 'Ужасы'

    def test_get_books_with_specific_genre_returns_matching_books(self):
        collector = BooksCollector()
        collector.add_new_book('Ревизор')
        collector.add_new_book('Вий')
        collector.set_book_genre('Ревизор', 'Комедии')
        collector.set_book_genre('Вий', 'Ужасы')
        assert collector.get_books_with_specific_genre('Комедии') == ['Ревизор']

    def test_get_books_genre_returns_current_dictionary(self):
        collector = BooksCollector()
        collector.add_new_book('Ревизор')
        collector.set_book_genre('Ревизор', 'Комедии')
        assert collector.get_books_genre() == {'Ревизор': 'Комедии'}

    @pytest.mark.parametrize(
        'genre, in_children',
        [
            ['Фантастика', True],
            ['Мультфильмы', True],
            ['Комедии', True],
            ['Ужасы', False],
            ['Детективы', False],
        ]
    )
    def test_get_books_for_children_filters_age_rating(self, genre, in_children):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.set_book_genre('Книга', genre)
        assert ('Книга' in collector.get_books_for_children()) is in_children

    def test_add_book_in_favorites_adds_book_only_once(self):
        collector = BooksCollector()
        collector.add_new_book('Ревизор')
        collector.add_book_in_favorites('Ревизор')
        collector.add_book_in_favorites('Ревизор')
        assert collector.get_list_of_favorites_books() == ['Ревизор']

    def test_delete_book_from_favorites_removes_book(self):
        collector = BooksCollector()
        collector.add_new_book('Ревизор')
        collector.add_book_in_favorites('Ревизор')
        collector.delete_book_from_favorites('Ревизор')
        assert collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books_returns_added_books(self):
        collector = BooksCollector()
        collector.add_new_book('Ревизор')
        collector.add_new_book('Вий')
        collector.add_book_in_favorites('Ревизор')
        collector.add_book_in_favorites('Вий')
        assert collector.get_list_of_favorites_books() == ['Ревизор', 'Вий']

    def test_add_new_book_same_name_added_once(self):
        collector = BooksCollector()
        collector.add_new_book('Ревизор')
        collector.add_new_book('Ревизор')
        assert collector.get_books_genre() == {'Ревизор': ''}

    @pytest.mark.parametrize(
        'name, genre',
        [
            ['Нет такой', 'Комедии'],
            ['Ревизор', 'Роман'],
        ]
    )
    def test_set_book_genre_missing_book_or_unknown_genre_not_set(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book('Ревизор')
        collector.set_book_genre(name, genre)
        assert collector.get_books_genre() == {'Ревизор': ''}

    def test_add_book_in_favorites_unknown_book_not_added(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Ревизор')
        assert collector.get_list_of_favorites_books() == []

    def test_get_books_for_children_book_without_genre_not_included(self):
        collector = BooksCollector()
        collector.add_new_book('Ревизор')
        assert collector.get_books_for_children() == []
