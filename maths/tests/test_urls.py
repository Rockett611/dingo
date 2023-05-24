from django.test import TestCase
from django.urls import resolve
from django.urls.exceptions import Resolver404
from maths.views import math_operation, maths_list, math_details, results_list


class TestUrls(TestCase):

    def test_resolution_for_add(self):
        resolver = resolve('/maths/add/1/2')
        self.assertEqual(resolver.func, math_operation)

    def test_resolution_for_sub(self):
        resolver = resolve('/maths/sub/1/2')
        self.assertEqual(resolver.func, math_operation)

    def test_arguments_should_be_integers_or_404(self):
        with self.assertRaises(Resolver404):
            resolve('maths/sub/a/b')

    def test_resolution_for_histories(self):
        resolver = resolve('/maths/histories/')
        self.assertEqual(resolver.func, maths_list)

    def test_resolution_for_histories_id(self):
        resolver = resolve('/maths/histories/2')
        self.assertEqual(resolver.func, math_details)

    def test_resolution_for_results(self):
        resolver = resolve('/maths/results/')
        self.assertEqual(resolver.func, results_list)