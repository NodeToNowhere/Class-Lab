import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer


class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Dave", 10, 42)
        self.customer1 = Customer("Ben", 50, 16)

    def test_has_customer(self):
        self.assertEqual("Dave", self.customer.name)

    def test_has_wallet(self):
        self.assertEqual(10, self.customer.wallet)

    def test_can_buy_drink(self):
        drink = Drink("wine",4.00)
        self.customer.buy_drink(drink)