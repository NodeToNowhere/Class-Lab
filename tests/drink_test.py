import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer


class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("Guiness", 25.00)

    def test_drink(self):
        self.assertEqual("Guiness", self.drink.name)
        self.assertEqual(25.00, self.drink.price)
