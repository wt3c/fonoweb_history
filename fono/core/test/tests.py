from django.test import TestCase
from django.shortcuts import resolve_url as r

class HomeTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('home'))

    def test_home(self):
        self.assertEqual(200, self.resp.status_code)
