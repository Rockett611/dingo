from django.contrib import admin

from posts.models import Post, Author
# Register your models here.


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'nick', 'email']
    list_filter =  ['nick', 'email']
    search_fields = ['nick', 'email']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', 'created', 'modified', 'author_id']
    list_filter = ['id', 'title', 'author_id']
    search_fields = ['id', 'title', 'content']
