from django.test import TestCase

from posts.models import Author


class AuthorModelTest(TestCase):

    def setUp(self):
        Author.objects.create(nick="x", email="x@xyz.pl")

    def test_author_str(self):
        a1 = Author.objects.get(nick="x")

        self.assertEqual(str(a1), "x, x@xyz.pl")

        # kreacja postów / __str__