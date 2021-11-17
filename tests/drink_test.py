import unittest

from src.drink import Drink


class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("Guiness", 5.00, 1)

    def test_drink(self):
        self.assertEqual("Guiness", self.drink.name)
        self.assertEqual(5.00, self.drink.price)
