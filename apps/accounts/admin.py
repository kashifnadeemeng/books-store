from django.contrib import admin
from apps.books.models import Category, Book


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')


class BookAdmin(admin.ModelAdmin):
    model = Category
    list_display = ('title', 'price', 'author', 'is_featured')
    search_fields = ('title', 'author', 'is_featured')
    list_filter = ('category', 'author', 'is_featured')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Book, BookAdmin)
