class Transaction:
    def __init__(self, amount, date, merchant, tag, id = None):
        self.amount = amount
        self.date = date
        self.merchant = merchant
        self.tag = tag
        self.id = id

    def amount_formatted(self):
        return '{:.2f}'.format(self.amount)