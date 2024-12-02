from . import models


def get_book_by_id(book_id: int) -> models.Book | None:
    """Get book by id"""

    try:
        query = models.Book.objects.get(id=book_id)
    except models.Book.DoesNotExist:
        query = None

    return query


def get_genre_by_name(genre_name: str) -> models.Genre | None:
    """Get genre by name"""

    try:
        query = models.Genre.objects.get(name=genre_name.strip())
    except models.Genre.DoesNotExist:
        query = None

    return query
