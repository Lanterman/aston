import datetime

from django.db import models
from django.urls import reverse

from config import settings


class Genre(models.Model):
    """Genre model"""

    name: str = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = "Genres"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('genre-detail', kwargs={'genre_name': self.name})


class Book(models.Model):
    """Book model"""

    name: str = models.CharField(max_length=100)
    genres: Genre = models.ManyToManyField(to=Genre)
    year_of_publication: str = models.CharField(max_length=4)
    author_id: int = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"

    def __str__(self):
        return f"{self.name} - author {self.author_id}"

    def get_absolute_url(self):
        return reverse('book-detail', kwargs={'book_id': self.id})