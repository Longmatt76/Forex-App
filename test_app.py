from unittest import TestCase
from app import *
from flask import session


class FlaskTests(TestCase):

    def setUp(self):
        """Stuff to do before every test."""

        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_homepage(self):
        """Tests the status code of the homepage and also if the html is properly displaying"""

        with app.test_client() as client:
            res = client.get('/')
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn(
                '<label for="convert-from" class="form-label">Converting from:</label>', html)

    def test_convert(self):
        """I need help with this one. It's attempting to test the convert function and also test the html 
        of the /convert page but it never gets there, the reponse that's returned is from index.html which
         means it must be getting caught by the "except" but Im not sure why because I'm providing all the 
         variables that it needs """
        with app.test_client() as client:
            res = client.post('/convert', data={'base_cur': "USD", 'dest_cur': "USD",
                                                "amount": int("1"), 'symbol_one': "&dollar;", 'symbol_two': "&dollar;"})
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn(
                '<p class="card-text fs-2"> $1.0 USD = $1.00 USD</p>', html)
