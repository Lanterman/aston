from datetime import datetime

from rest_framework import serializers

from . import models


class BaseGenreSerializer(serializers.ModelSerializer):
    """Base genre serializer"""

    url = serializers.HyperlinkedIdentityField(view_name='genre-detail', lookup_field='name')

    class Meta:
        model = models.Genre
        fields = ["id", "url", "name"]


class BaseBookSerializer(serializers.ModelSerializer):
    """Base book serializer"""

    url = serializers.HyperlinkedIdentityField(view_name='book-detail', lookup_field='id')

    class Meta:
        model = models.Book
        fields = ["id", "url", "name", "year_of_publication", "author_id"]


class BookSerializer(serializers.ModelSerializer):
    """Book serializer"""

    url = serializers.HyperlinkedIdentityField(view_name='book-detail', lookup_field='id')
    genres = BaseGenreSerializer(many=True)

    class Meta:
        model = models.Book
        fields = ["id", "url", "name", "year_of_publication", "author_id", "genres"]


class CreateUpdateBookSerializer(serializers.ModelSerializer):
    """Create/update book serializer"""

    class Meta:
        model = models.Book
        fields = ["id", "name", "year_of_publication"]
    
    def validate_year_of_publication(self, value: str) -> str:
        min_year = 1700
        current_year = int(datetime.now().strftime("%Y"))
        
        if value > current_year:
            value = current_year
        
        elif value < min_year:
            value = min_year
        
        return value


class GenreListSerializer(serializers.ModelSerializer):
    """Genre list serializer"""

    url = serializers.HyperlinkedIdentityField(view_name='genre-detail', lookup_field='name')

    class Meta:
        model = models.Genre
        fields = ["id", "url", "name"]
        extra_kwargs = {"url": {"read_only": True}}


class GenreSerializer(serializers.ModelSerializer):
    """Genre serializer"""

    book_set = BaseBookSerializer(many=True)

    class Meta:
        model = models.Genre
        fields = ["id", "name", "book_set"]


class AddGenreToBookSerializer(serializers.ModelSerializer):
    """Add genre to book serializer"""

    class Meta:
        model = models.Genre
        fields = ["name"]
