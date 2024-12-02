from django.utils.decorators import method_decorator
from rest_framework import generics, status, response, exceptions
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema

from . import models, serializers, db_queries, permissions


@method_decorator(name="get", decorator=swagger_auto_schema(tags=["books"]))
@method_decorator(name="post", decorator=swagger_auto_schema(tags=["books"]))
class BookListView(generics.ListCreateAPIView):
    """Get book list and ceate book endpoints"""

    queryset = models.Book.objects.all().prefetch_related("genres")
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self, *args, **kwargs):
        if self.request.method == "GET":
            return serializers.BookSerializer
        return serializers.CreateUpdateBookSerializer

    def perform_create(self, serializer):
        serializer.save(author_id_id=self.request.user.id)


@method_decorator(name="get", decorator=swagger_auto_schema(tags=["book"]))
@method_decorator(name="put", decorator=swagger_auto_schema(tags=["book"]))
@method_decorator(name="patch", decorator=swagger_auto_schema(tags=["book"], deprecated=True))
@method_decorator(name="delete", decorator=swagger_auto_schema(tags=["book"]))
class BookView(generics.RetrieveUpdateDestroyAPIView):
    """Get, update and delete book endpoints"""

    lookup_field = "id"

    def get_queryset(self):
        if self.request.method == "GET":
            return models.Book.objects.all().prefetch_related("genres")
        return models.Book.objects.all()
    
    def get_permissions(self):
        permission_list = [IsAuthenticated]
        
        if self.request.method in ("PUT", "PATCH", "DELETE"):
            permission_list.append(permissions.IsOwner)
        
        return [permission() for permission in permission_list]

    def get_serializer_class(self, *args, **kwargs):
        if self.request.method == "GET":
            return serializers.BookSerializer
        return serializers.CreateUpdateBookSerializer


@method_decorator(name="put", decorator=swagger_auto_schema(tags=["book"]))
@method_decorator(name="patch", decorator=swagger_auto_schema(tags=["book"], deprecated=True))
class AddGenreToBookView(generics.UpdateAPIView):
    """Add genre to book endpoint"""

    permission_classes = [IsAuthenticated, permissions.IsOwner]
    serializer_class = serializers.AddGenreToBookSerializer
    queryset = models.Book.objects.all()
    lookup_field = "id"

    def put(self, request, *args, **kwargs):
        current_book = self.get_object()
        current_genre = db_queries.get_genre_by_name(request.data["name"])

        if not current_genre:
            raise exceptions.NotFound(detail="No such genre found!", code=status.HTTP_404_NOT_FOUND)
        
        current_book.genres.add(current_genre)
        return response.Response(data={"detail": f"{current_genre.name} genre was added to {current_book.name} book!"})


@method_decorator(name="get", decorator=swagger_auto_schema(tags=["genres"]))
@method_decorator(name="post", decorator=swagger_auto_schema(tags=["genres"]))
class GenresListView(generics.ListCreateAPIView):
    """Get genres list and create genre endpoints"""

    queryset = models.Genre.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.GenreListSerializer


@method_decorator(name="get", decorator=swagger_auto_schema(tags=["genre"]))
class GenreView(generics.RetrieveAPIView):
    """Get genre endpoint"""

    queryset = models.Genre.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.GenreSerializer
    lookup_field = "name"
