from django.urls import path

from . import views

urlpatterns = [
    path("books/", views.BookListView.as_view(), name="book-list"),
    path("books/<int:id>", views.BookView.as_view(), name="book-detail"),
    path("books/<int:id>/add_genre", views.AddGenreToBookView.as_view(), name="add_genre_to_book"),
    path("genres/", views.GenresListView.as_view(), name="genre-list"),
    path("genres/<str:name>", views.GenreView.as_view(), name="genre-detail")
]