from django.test import TestCase
from django.urls import resolve

from posts.views import posts_list, post_details, add_post, authors_list, authors_details


class TestUrls(TestCase):

    def test_resolution_for_posts_list(self):
        resolver = resolve('/posts/')
        self.assertEqual(resolver.func, posts_list)

    def test_resolution_for_posts_details(self):
        resolver = resolve('/posts/1')
        self.assertEqual(resolver.func, post_details)

    def test_resolution_for_add_post(self):
        resolver = resolve('/posts/add/')
        self.assertEqual(resolver.func, add_post)

    def test_resolution_for_authors_list(self):
        resolver = resolve('/posts/authors/all')
        self.assertEqual(resolver.func, authors_list)

    def test_resolution_for_authors_details(self):
        resolver = resolve('/posts/authors/1')
        self.assertEqual(resolver.func, authors_details)