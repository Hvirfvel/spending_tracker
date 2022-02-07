class Transaction:
    def __init__(self, amount, date, merchant, tag, id = None):
        self.amount = amount
        self.date = date
        self.merchant = merchant
        self.tag = tag
        self.id = id

    def get_total(transactions):
        total = 0
        for transaction in transactions:
            total += transaction.amount
        return round(total, 2)

    def get_date(transaction):
        return transaction.date

    def sort_by_date(transactions):
        transactions_by_date = sorted(transactions, key=Transaction.get_date, reverse=True)
        return transactions_by_date