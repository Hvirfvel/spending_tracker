def get_total(transactions):
        total = 0
        for transaction in transactions:
            total += transaction.amount
        return round(total, 2)

def get_date(transaction):
    return transaction.date

def sort_by_date(transactions):
    return sorted(transactions, key=get_date, reverse=True)