import unittest
from models.transaction import Transaction

class TestTransaction(unittest.TestCase):
    def setUp(self):
        self.transaction = Transaction(21.50, '12/12/2021', 'Aldi', 'Groceries')
        

    def test_get_total_amount(self):
        transaction2 = Transaction(12.30, '22/12/2021', 'Boots', 'Pharmacy')
        transactions = [self.transaction, transaction2]
        self.assertEqual(33.80, self.transaction.get_total(transactions))