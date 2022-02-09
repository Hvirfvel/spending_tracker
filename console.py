import pdb
from models.merchant import Merchant
from models.tag import Tag
from models.transaction import Transaction

import repositories.merchant_repository as merchant_repository
import repositories.tag_repository as tag_repository
import repositories.transaction_repository as transaction_repository

from datetime import datetime

transaction_repository.delete_all()
merchant_repository.delete_all()
tag_repository.delete_all()

merchant_1 = Merchant('Aldi')
merchant_repository.save(merchant_1)

tag_1 = Tag('Groceries')
tag_repository.save(tag_1)

transaction_1 = Transaction(14.99, '2022-01-27', merchant_1, tag_1)
transaction_repository.save(transaction_1)

print(transaction_1.__dict__)

new_date = datetime.strptime(transaction_1.date, '%Y-%m-%d').month
print(new_date)

month = 1

print(transaction_repository.transactions_by_month(month)[0].__dict__)


pdb.set_trace()