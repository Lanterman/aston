from django.urls import path, include
from rest_framework import permissions
from rest_framework.settings import api_settings
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from . import settings
from apps.user.auth.backends import JWTTokenAuthBackend


AUTH_HEADER_TYPES = settings.JWT_SETTINGS["AUTH_HEADER_TYPES"]

contact = openapi.Contact(name="Lanterman", url="https://github.com/Lanterman", email='klivchinskydmitry@gmail.com')

schema_url_patterns = [
   path("api/v1/", include('apps.urls')),
]

description = f"""
For authenticated requests, create a user and enter the resulting token along with the word '{AUTH_HEADER_TYPES}'.
Example: '{AUTH_HEADER_TYPES} eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjozLCJ0eXBlX3Rva2VuIjoiYWNjZXNzIn0.6wic2W1-8cGqJVYbTzuLKNIdXPwjUQvNc0TjhwP5FXc'.

P.S.
Before resetting "auth/reset_password/<user_email>/<user_secret_key>/" password, you must request it from "/auth/profile/try_to_reset_password/" endpoint.
"""

schema_view = get_schema_view(
   openapi.Info(
      title="ASTON test",
      default_version=api_settings.DEFAULT_VERSION,
      description=description,
      license=openapi.License(name="BSD License"),
      contact=contact,
   ),
   public=True,
   patterns=schema_url_patterns,
   permission_classes=[permissions.AllowAny],
   authentication_classes=[JWTTokenAuthBackend]
)

urlpatterns = [
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]