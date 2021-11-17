import unittest

from src.customer import Customer

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Dave", 10.0, 42.0)

    def test_has_customer(self):
        self.assertEqual("Dave", self.customer.name)

    def test_has_wallet(self):
        self.assertEqual(10.0, self.customer.wallet)

    def test_reduce_wallet(self):
        self.customer.reduce_wallet(5.0)
        self.assertEqual(5.0, self.customer.wallet)
