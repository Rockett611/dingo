from rest_framework import routers

from books import api_views as book_views
from posts import api_views as posts_views

router = routers.DefaultRouter()
router.register('posts', posts_views.PostViewset)
router.register('authors', posts_views.AuthorViewset)

router.register('books', book_views.BookViewset)
router.register('book_authors', book_views.BookAuthorViewset)