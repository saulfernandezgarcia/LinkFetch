from unittest import TestCase

from src.main import Cat

class TestCat(TestCase):
    def test_meow(self):
        self.assertEqual(Cat.meow(self), "meow")