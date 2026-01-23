from .models import CustomUser
from django.contrib import admin
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Columns shown in the admin list view
    list_display = ('title', 'author', 'publication_year')

    # Filters that appear on the right sidebar
    list_filter = ('publication_year', 'author')

    # Search box functionality
    search_fields = ('title', 'author')


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "date_of_birth", "is_staff")
