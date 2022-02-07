import pdb
from models.merchant import Merchant
from models.tag import Tag
from models.transaction import Transaction

import repositories.merchant_repository as merchant_repository
import repositories.tag_repository as tag_repository
import repositories.transaction_repository as transaction_repository

transaction_repository.delete_all()
merchant_repository.delete_all()
tag_repository.delete_all()

merchant_1 = Merchant('Aldi')
merchant_repository.save(merchant_1)

# merchants = merchant_repository.select_all()

# for merchant in merchants:
#     print(merchant.__dict__)

tag_1 = Tag('Groceries')
tag_repository.save(tag_1)

# tags = tag_repository.select_all()

# for tag in tags:
#     print(tag.__dict__)

transaction_1 = Transaction(14.99, '2022-01-27', merchant_1, tag_1)
transaction_repository.save(transaction_1)

print(transaction_1.__dict__)

# transactions = transaction_repository.transactions_by_tag(tag_1)
# print(transactions)

transactions = transaction_repository.transactions_by_merchant(merchant_1)
print(transactions)


pdb.set_trace()