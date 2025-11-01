import pytest
from main import BooksCollector  

@pytest.fixture
def collector():
    """Фикстура для создания экземпляра класса BooksCollector."""
    return BooksCollector()
