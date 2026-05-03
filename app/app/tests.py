from django.test import SimpleTestCase
from . import calc


class test_number(SimpleTestCase):    
    def test_add_numbers(self):
        res = calc.calcu(6,5)
        self.assertEqual(res, 11)

    def testa_add_numbers(self):
        res = calc.subtra(10,15)
        self.assertEqual(res, 5)
