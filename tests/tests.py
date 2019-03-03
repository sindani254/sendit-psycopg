import unittest

from flask_testing import TestCase
from app import app

BASE_URL = "http://127.0.0.1:5000/api/v1"
ORDERS_URL = '{}/orders'.format(BASE_URL)
BAD_ITEM_URL = '{}/5'.format(BASE_URL)
GOOD_ITEM_URL = '{}/2'.format(BASE_URL)


class BaseTestCase(TestCase):
    """docstring for FlaskTestCase"""

    def create_app(self):
        app.config.from_object("config.DevConfig")
        return app


class FlaskTestCase(BaseTestCase):
    """docstring for FlaskTestCase"""

    def test_get_all_orders(self):
        response = self.client.get(ORDERS_URL, content_type="application/json")
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
