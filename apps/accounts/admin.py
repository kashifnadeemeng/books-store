from django.contrib import admin
from apps.books.models import Category, Book


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('category', 'title', 'price', 'author', 'is_featured')
    search_fields = ('title', 'author', 'is_featured')
    list_filter = ('category', 'author', 'is_featured')
