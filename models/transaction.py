class Transaction:
    def __init__(self, amount, date, merchant, tag, id = None):
        self.amount = amount
        self.date = date
        self.merchant = merchant
        self.tag = tag
        self.id = id

    def amount_formatted(self):
        return '{:.2f}'.format(self.amount)

    def get_total(transactions):
        total = 0
        for transaction in transactions:
            total += transaction.amount
        return round(total, 2)

    def get_date(transaction):
        return transaction.date

    def sort_by_date(transactions):
        return sorted(transactions, key=Transaction.get_date, reverse=True)