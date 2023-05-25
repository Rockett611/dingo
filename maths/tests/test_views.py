from django.test import TestCase, Client
from django.utils.datetime_safe import datetime

from maths.models import Math


class MathViewsTest(TestCase):

    def setUp(self):
        Math.objects.create(operation="sub", a=20, b=30)
        self.client = Client()

    def test_maths_list(self):
        response = self.client.get("/maths/histories/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["maths"]), 1)
        self.assertIn('<li><a href="/maths/histories/1">id:1, a=20, b=30, op=sub</a></li>', response.content.decode())

    def test_maths_operation(self):
        response = self.client.get("/maths/sub/20/30")
        self.assertEqual(response.status_code, 200)
        self.assertIn \
            ('<!DOCTYPE html>\n<html lang="en">\n<head>\n   <meta charset="UTF-8">\n   <title>sub</title>\n</head>\n<body>\n    <div id="content">\n        <div id="header">\n            Część wspólna.\n        </div>\n        <div id="inner-content">\n            \n   Wynik operacji 20 - 30 wynosi -10\n\n        </div>\n    </div>\n</body>\n</html>\n',
             response.content.decode())

    def test_maths_details(self):
        response = self.client.get("/maths/histories/1")
        self.assertEqual(response.status_code, 200)

    #         self.assertIn('<!DOCTYPE html>\n<html lang="en">\n<head>\n   <meta charset="UTF-8">\n   <title>Maths lis'
    # 't</title>\n</head>\n<body>\n    <div id="content">\n        <div id="header">\n            Część ws'
    # 'pólna.\n        </div>\n        <div id="inner-content">\n            \n   <table>\n       <tr>\n'
    #          '<th>Operation</th>\n           <td>sub</td>\n       </tr>\n       <tr>\n           <th>a</'
    # 'th>\n           <td>20</td>\n       </tr>\n       <tr>\n           <th>b</th>\n           <td>30</t'
    # f'd>\n       </tr>\n       <tr>\n           <th>Created:</th>\n           <td>{datetime.now()}'
    # '</td>\n       </tr>\n       <tr>\n           <th>Result</th>\n           <td>value: -10.0 | error: None</td>\n       </t'
    # 'r>\n   </table>\n   <a href="/maths/histories/">back</a>\n\n        </div>\n    </div>\n</body>\n</html>\n', response.content.decode())

    def test_result_list(self):
        response = self.client.get("/maths/results/")
        self.assertEqual(response.status_code, 200)
        # self.assertIn('<!DOCTYPE html>\n<html lang="en">\n<head>\n   <meta charset="UTF-8">\n   <title>Maths list</title>\n</head>\n<body>\n    <div id="content">\n        <div id="header">\n            Cz\xc4\x99\xc5\x9b\xc4\x87 wsp\xc3\xb3lna.\n        </div>\n        <div id="inner-content">\n\n   <ul>\n       \n           <li>value: None | error: ZeroDivisionError</li>\n       \n <li>value: 3.0 | error: None</li>\n       \n           <li>value: 5484.0 | error: None</li>\n  \n           <li>value: 55.0 | error: None</li>\n       \n           <li>value: 7744.0 | error: None</li>\n       \n           <li>value: 48.0 | error: None</li>\n       \n           <li>value: 634.0 | error: None</li>\n       \n           <li>value: 16.0 | error: None</li>\n       \n <li>value: 723.0 | error: None</li>\n       \n           <li>value: -10.0 | error: None</li>\n   \n   </ul>\n\n   <form method="post">\n   <input type="hidden" name="csrfmiddlewaretoken" value="LLqQpcAUW1TR8s2dO6o2x5HQdTftR9m7DgmJ0mBnXxqj40gTxGGE0L2DlJMcil3v">\n   <tr>\n    <th><label for="id_value">Value:</label></th>\n    <td>\n      \n      <input type="number" name="value" step="any"id="id_value">\n      \n      \n    </td>\n  </tr>\n\n  <tr>\n    <th><label for="id_error">Error:</label></th>\n    <td>\n      \n      <input type="text" name="error" maxlength="255" id="id_error">\n      \n      \n        \n      \n    </td>\n  </tr>\n   <input type="submit" value="go">\n</form>\n\n\n\n        </div>\n    </div>\n</body>\n</html>\n', response.content.decode())


class MathViewsPaginationTest(TestCase):
    fixtures = ['math', 'result']

    def setUp(self):
        self.client = Client()

    def test_get_first_5(self):
        response = self.client.get("/maths/histories/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["maths"]), 5)

    def test_get_last_page(self):
        response = self.client.get("/maths/histories/?page=3")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["maths"]), 1)
