import unittest
from models.transaction import Transaction

class TestTransaction(unittest.TestCase):
    def setUp(self):
        self.transaction = Transaction(21.5, '12/12/2021', 'Aldi', 'Groceries')
        

    # def test_get_total_amount(self):
    #     transaction2 = Transaction(12.30, '22/12/2021', 'Boots', 'Pharmacy')
    #     transactions = [self.transaction, transaction2]
    #     self.assertEqual(33.80, self.transaction.get_total(transactions))

    # def test_sort_by_date(self):
    #     transaction2 = Transaction(13.40, '21/12/2021', 'Londis', 'Fuel')
    #     transactions = [self.transaction, transaction2]
    #     self.assertEqual([transaction2, self.transaction], self.transaction.sort_by_date(transactions))

    def test_formatted_amount(self):
        self.assertEqual('21.50', self.transaction.amount_formatted())