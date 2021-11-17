import unittest
from unittest.case import TestCase
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer


class TestPub(unittest.TestCase):
    # look at unittest docs to see what they do!
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00)
        self.customer1 = Customer("Dave", 200.00, 42)
        self.customer2 = Customer("Ben", 50, 16)
        self.customer3 = Customer("Andy", 0, 22)
        self.drink = Drink("Guiness", 5.00, 1)

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_increase_till(self):
        # arrange
        # act
        self.pub.increase_till(2.50)
        # assert
        expected = 102.5
        actual = self.pub.till
        self.assertEqual(expected, actual)  # explicit: remember/try this

    def test_add_drink(self):
        self.pub.add_drink(self.drink)

    def test_check_age(self):
        self.assertEqual(self.pub.check_age(self.customer1), True)
        self.assertEqual(self.pub.check_age(self.customer2), False)

    def test_sell_drink(self):
        self.pub.sell_drink(self.customer1, self.drink)
        self.assertEqual(self.customer1.wallet, 195.0)
        self.assertEqual(self.pub.till, 105.0)
