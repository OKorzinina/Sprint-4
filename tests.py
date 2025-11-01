import pytest
from main import BooksCollector


class TestBooksCollector:

    @pytest.fixture
    def collector(self):
        return BooksCollector()

    # Проверяет, что новая книга добавляется в коллекцию.
    def test_add_new_book(self, collector):
        collector.add_new_book('Гордость и предубеждение')
        assert 'Гордость и предубеждение' in collector.books_genre

    # Проверяет, что книга с названием длиннее 40 символов не добавляется.
    def test_add_book_with_long_name(self, collector):
        collector.add_new_book('Очень длинное название книги, которое больше 40 символов')
        assert 'Очень длинное название книги, которое больше 40 символов' not in collector.books_genre

    # Проверяет, что одну и ту же книгу нельзя добавить дважды.
    def test_add_same_book_twice(self, collector):
        collector.add_new_book('Гордость и предубеждение')
        collector.add_new_book('Гордость и предубеждение')
        assert list(collector.books_genre.keys()).count('Гордость и предубеждение') == 1

    # Проверяет, что жанр книги устанавливается корректно.
    def test_set_book_genre(self, collector):
        collector.add_new_book('Гордость и предубеждение')
        collector.set_book_genre('Гордость и предубеждение', 'Комедии')
        assert collector.get_book_genre('Гордость и предубеждение') == 'Комедии'

    # Проверяет, что нельзя установить жанр для несуществующей книги.
    def test_set_genre_for_non_existing_book(self, collector):
        collector.set_book_genre('Неизвестная книга', 'Фантастика')
        assert collector.get_book_genre('Неизвестная книга') is None

    # Проверяет, что при установке некорректного жанра, жанр не меняется (остается пустым).
    def test_set_book_genre_invalid_genre(self, collector):
        collector.add_new_book('Гордость и предубеждение')
        collector.set_book_genre('Гордость и предубеждение', 'Триллер')
        assert collector.get_book_genre('Гордость и предубеждение') == ''

    # Проверяет, что жанр книги возвращается корректно.
    def test_get_book_genre(self, collector):
        collector.add_new_book('Гордость и предубеждение')
        collector.set_book_genre('Гордость и предубеждение', 'Комедии')
        assert collector.get_book_genre('Гордость и предубеждение') == 'Комедии'

    # Проверяет, что возвращается список книг определенного жанра.
    @pytest.mark.parametrize('genre, expected_books', [
        ('Фантастика', ['Гарри Поттер']),
        ('Ужасы', ['Звонок'])
    ])
    def test_get_books_with_specific_genre(self, collector, genre, expected_books):
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        collector.add_new_book('Звонок')
        collector.set_book_genre('Звонок', 'Ужасы')
        assert collector.get_books_with_specific_genre(genre) == expected_books

    # Проверяет, что возвращается список книг для детей (без учета "Ужасов").
    def test_get_books_for_children(self, collector):
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        collector.add_new_book('Звонок')
        collector.set_book_genre('Звонок', 'Ужасы')
        assert collector.get_books_for_children() == ['Гарри Поттер']

    # Проверяет добавление книги в избранное.
    def test_add_book_in_favorites(self, collector):
        collector.add_new_book('Гордость и предубеждение')
        collector.add_book_in_favorites('Гордость и предубеждение')
        assert 'Гордость и предубеждение' in collector.get_list_of_favorites_books()

    # Проверяет, что нельзя добавить в избранное несуществующую книгу.
    def test_add_non_existing_book_in_favorites(self, collector):
        collector.add_book_in_favorites('Неизвестная книга')
        assert 'Неизвестная книга' not in collector.get_list_of_favorites_books()

    # Проверяет, что одну и ту же книгу нельзя добавить в избранное дважды.
    def test_add_the_same_book_twice_in_favorites(self, collector):
        collector.add_new_book('Гордость и предубеждение')
        collector.add_book_in_favorites('Гордость и предубеждение')
        collector.add_book_in_favorites('Гордость и предубеждение')
        assert collector.get_list_of_favorites_books().count('Гордость и предубеждение') == 1

    # Проверяет удаление книги из избранного.
    def test_delete_book_from_favorites(self, collector):
        collector.add_new_book('Гордость и предубеждение')
        collector.add_book_in_favorites('Гордость и предубеждение')
        collector.delete_book_from_favorites('Гордость и предубеждение')
        assert 'Гордость и предубеждение' not in collector.get_list_of_favorites_books()

    # Проверяет, что нельзя удалить из избранного несуществующую книгу.
    def test_delete_non_existing_book_from_favorites(self, collector):
        collector.delete_book_from_favorites('Неизвестная книга')
        assert 'Неизвестная книга' not in collector.get_list_of_favorites_books()

    # Проверяет получение списка избранных книг.
    def test_get_list_of_favorites_books(self, collector):
        collector.add_new_book('Гордость и предубеждение')
        collector.add_book_in_favorites('Гордость и предубеждение')
        assert collector.get_list_of_favorites_books() == ['Гордость и предубеждение']

