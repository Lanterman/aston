from django.contrib import admin

from . import models


@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):
    """Genre admin"""

    list_display = ("id", "name")
    list_display_links = ("id", "name")
    fields = ("name",)
    search_fields = ("name",)
    list_max_show_all = 250
    list_per_page = 150


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    """Book admin"""

    list_display = ("id", "name", "year_of_publication", "author_id")
    list_display_links = ("id", "name", "year_of_publication", "author_id")
    fields = ("name", "year_of_publication", "author_id", "genres")
    list_max_show_all = 250
    list_per_page = 150
    raw_id_fields = ("genres", )
