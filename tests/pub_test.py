import unittest
from unittest.case import TestCase
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer


class TestPub(unittest.TestCase):
    # look at unittest docs to see what they do!
    def setUp(self):
        drinks = {"Guiness": 25.00}
        self.pub = Pub("The Prancing Pony", 100.00, drinks)
        self.customer1 = Customer("Dave", 200.00, 42)
        self.customer2 = Customer("Ben", 50, 16)
        self.drink = Drink("Guiness", 25.00)

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_increase_till(self):
        # arrange
        # act
        self.pub.increase_till(2.50)
        # assert
        expected = 102.5
        actual = self.pub.till
        self.assertEqual(expected, actual)

    def test_check_age(self):
        self.assertEqual(self.pub.check_age(customer1), True)
        self.assertEqual(self.pub.check_age(customer2), False)
