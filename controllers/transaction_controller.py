from flask import Flask, Blueprint, redirect, render_template, request
from models.transaction import Transaction
import repositories.transaction_repository as transaction_repository
import repositories.merchant_repository as merchant_repository
import repositories.tag_repository as tag_repository
import helpers.transaction_helper as transaction_helper
from helpers.months import months

transactions_blueprint = Blueprint('transactions', __name__)

@transactions_blueprint.route('/transactions')
def index():
    merchants = merchant_repository.select_all()
    transactions = transaction_repository.select_all()
    total = transaction_helper.get_total(transactions)
    transactions_by_date = transaction_helper.sort_by_date(transactions)
    return render_template('transactions/index.html', transactions_by_date=transactions_by_date, total=total, merchants=merchants)

@transactions_blueprint.route('/transactions/new')
def new_transaction():
    merchants = merchant_repository.select_all()
    tags = tag_repository.select_all()
    return render_template('transactions/new.html', merchants=merchants, tags=tags)

@transactions_blueprint.route('/transactions/new', methods=['POST'])
def create_transaction():
    amount = request.form['amount']
    date = request.form['date']
    merchant_id = request.form['merchant_id']
    tag_id = request.form['tag_id']
    merchant = merchant_repository.select(merchant_id)
    tag = tag_repository.select(tag_id)

    transaction = Transaction(amount, date, merchant, tag)
    transaction_repository.save(transaction)
    return redirect('/transactions')

@transactions_blueprint.route('/transactions/tags/<id>')
def show_by_tag(id):
    tag = tag_repository.select(id)
    transactions = transaction_repository.transactions_by_tag(tag)
    total = transaction_helper.get_total(transactions)
    transactions_by_date = transaction_helper.sort_by_date(transactions)
    return render_template('transactions/index.html', transactions_by_date=transactions_by_date, total=total)

@transactions_blueprint.route('/transactions/merchants/<id>')
def show_by_merchants(id):
    merchant = merchant_repository.select(id)
    transactions = transaction_repository.transactions_by_merchant(merchant)
    total = transaction_helper.get_total(transactions)
    transactions_by_date = transaction_helper.sort_by_date(transactions)
    return render_template('transactions/index.html', transactions_by_date=transactions_by_date, total=total)

@transactions_blueprint.route('/transactions/month/<number>')
def show_by_month(number):
    transactions = transaction_repository.transactions_by_month(number)
    total = transaction_helper.get_total(transactions)
    transactions_by_date = transaction_helper.sort_by_date(transactions)
    return render_template('transactions/index.html', transactions_by_date=transactions_by_date, total=total)
    
    
