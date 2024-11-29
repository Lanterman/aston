from django.utils.decorators import method_decorator
from rest_framework import generics, status, response
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema

from . import models, serializers, services, db_queries


@method_decorator(name="get", decorator=swagger_auto_schema(tags=["books"]))
@method_decorator(name="post", decorator=swagger_auto_schema(tags=["books"]))
class BookListView(generics.ListCreateAPIView):
    """Book list endpoint"""

    queryset = models.Book.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.BookSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        print(request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return response.Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)