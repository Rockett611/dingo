from django.test import TestCase

from posts.forms import PostForm, AuthorForm
from posts.models import Post, Author


# class PostFormTest(TestCase):

    # def test_post_save_correct_data(self):
    #     data = {"title": "xxx",
    #             "content": "yyy",
    #             "author": "maupa, maupa@djungla.pl"}
    #     self.assertEqual(len(Post.objects.all()), 0)
    #     form = PostForm(data=data)
    #     self.assertTrue(form.is_valid())
    #     p = form.save()
    #     self.assertIsInstance(p, Post)
    #     self.assertEqual(p.title, "xxx")
    #     self.assertIsNotNone(p.id)

# class AuthorFormTest(TestCase):

    # def test_author_save_correct_data(self):
    #     data = {"nick": "x", "email": "x@xyz.pl"}
    #     self.assertEqual(len(Post.objects.all()), 0)
    #     form = AuthorForm(data=data)
    #     self.assertTrue(form.is_valid())
    #     a = form.save()
    #     self.assertIsInstance(a, Author)
    #     self.assertEqual(a.nick, "x")
    #     self.assertIsNotNone(a.id)

    # form is not valid