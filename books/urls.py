from django.urls import path

from .views import book_list, book_details, author_list, author_details

app_name = 'books'
urlpatterns = [
    path('', book_list, name='books_list'),
    path('<id>', book_details, name='book_details'),
    path('authors/all', author_list, name='authors_list'),
    path('authors/<id>', author_details, name='author_details'),
]
