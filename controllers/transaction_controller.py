from flask import Flask, Blueprint, render_template
from models.transaction import Transaction
import repositories.transaction_repository as transaction_repository

transactions_blueprint = Blueprint('transactions', __name__)

@transactions_blueprint.route('/transactions')
def index():
    transactions = transaction_repository.select_all()
    return render_template('transactions/index.html', transactions=transactions)