from django.test import TestCase, Client

from posts.models import Author


class AuthorViewsTest(TestCase):

    def setUp(self):
        Author.objects.create(nick="x", email="x@xyz.pl")
        self.client = Client()

    def test_authors_details(self):
        response = self.client.get("/posts/authors/1")
        self.assertEqual(response.status_code, 200)

# html nie przechodzi