import re

from rest_framework import serializers, status

from . import models


class BaseGenreSerializer(serializers.ModelSerializer):
    """Base genre serializer"""

    class Meta:
        model = models.Book
        fields = ["id", "name"]


class BaseBookSerializer(serializers.ModelSerializer):
    """Base book serializer"""


    class Meta:
        model = models.Book
        fields = ["id", "name", "year_of_publication", "author_id"]


class BookSerializer(serializers.ModelSerializer):
    """Book serializer"""

    genres = BaseGenreSerializer(many=True)

    class Meta:
        model = models.Book
        fields = ["id", "name", "year_of_publication", "author_id", "genres"]
        extra_kwargs = {"author_id": {"read_only": True}}