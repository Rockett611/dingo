from django.urls import path

from .views import posts_list, post_details, add_post, authors_list, authors_details


app_name = 'posts'
urlpatterns = [
    path('', posts_list, name='posts_list'),
    path('<id>', post_details, name='post_details'),
    path('add/', add_post, name="add_post"),
    path('authors/all', authors_list, name='authors_list'),
    path('authors/<id>', authors_details, name='author_details')
]

