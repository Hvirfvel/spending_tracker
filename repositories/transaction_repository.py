from db.run_sql import run_sql
from models.transaction import Transaction
import repositories.merchant_repository as merchant_repository
import repositories.tag_repository as tag_repository

def save(transaction):
    sql = """
    INSERT INTO transactions 
    (amount, date, merchant_id, tag_id) 
    VALUES (%s, %s, %s, %s)
    RETURNING id
    """
    values = [
        transaction.amount, 
        transaction.date, 
        transaction.merchant.id,
        transaction.tag.id]
    results = run_sql(sql, values)
    transaction.id = results[0]['id']
    return transaction
    

def select_all():
    transactions = []
    sql = "SELECT * FROM transactions"
    results = run_sql(sql)

    for row in results:
        merchant = merchant_repository.select(row['merchant_id'])
        tag = tag_repository.select(row['tag_id'])
        
        transaction = Transaction(
            row['amount'],
            row['date'],
            merchant,
            tag,
            row['id'])
        transactions.append(transaction)
    return transactions


def delete_all():
    sql = "DELETE FROM transactions"
    run_sql(sql)


def transactions_by_tag(tag):
    transactions = []

    sql = "SELECT * FROM transactions WHERE tag_id = %s"
    values = [tag.id]
    results = run_sql(sql, values)
    for row in results:
        merchant = merchant_repository.select(row['merchant_id'])
        transaction = Transaction(row['amount'], row['date'], merchant, tag, row['id'])
        transactions.append(transaction)
    return transactions


def transactions_by_merchant(merchant):
    transactions = []

    sql = "SELECT * FROM transactions WHERE merchant_id = %s"
    values = [merchant.id]
    results = run_sql(sql, values)
    for row in results:
        tag = tag_repository.select(row['tag_id'])
        transaction = Transaction(row['amount'], row['date'], merchant, tag, row['id'])
        transactions.append(transaction)
    return transactions


def transactions_by_month(month):
    transactions = []

    sql = "SELECT * FROM transactions WHERE DATE_PART('MONTH', date) = %s"
    values = [month]
    results = run_sql(sql, values)

    for row in results:
        merchant = merchant_repository.select(row['merchant_id'])
        tag = tag_repository.select(row['tag_id'])
        
        transaction = Transaction(
            row['amount'],
            row['date'],
            merchant,
            tag,
            row['id'])
        transactions.append(transaction)
    return transactions