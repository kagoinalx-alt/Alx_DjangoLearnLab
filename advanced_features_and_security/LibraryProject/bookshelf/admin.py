from django.contrib.auth.admin import UserAdmin
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


class CustomUserAdmin(UserAdmin):
    model = CustomUser

    fieldsets = UserAdmin.fieldsets + (
        ("Additional Info", {
            "fields": ("date_of_birth", "profile_photo"),
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional Info", {
            "fields": ("date_of_birth", "profile_photo"),
        }),
    )

    list_display = ("username", "email", "date_of_birth",
                    "is_staff", "is_active")
    search_fields = ("username", "email")
    ordering = ("username",)


admin.site.register(CustomUser, CustomUserAdmin)
