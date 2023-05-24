from django.test import TestCase, Client

class GreetiengsViewsTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_greetings(self):
        response = self.client.get('/greetings/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Hello World!', response.content.decode())

    def test_greetings_name(self):
        response = self.client.get('/greetings/Edward')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Hello Edward', response.content.decode())
