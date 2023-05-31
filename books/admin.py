from django.contrib import admin

# Register your models here.
from books.models import Book, Author, Tag, BorrowTwo


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author']
    list_filter = ['id', 'title', 'author']
    search_fields =  ['id', 'title']


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'is_active']
    list_filter = ['id', 'full_name']
    search_fields = ['id', 'full_name']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(BorrowTwo)
class BorrowAdmin(admin.ModelAdmin):
    list_display = ['book', 'user', 'rental_date', 'is_returned']
    list_filter = ['book', 'user', 'is_returned']
    search_fields = ['book', 'user', 'rental_date', 'is_returned']

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)
