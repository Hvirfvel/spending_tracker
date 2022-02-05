import pdb
from models.merchant import Merchant
from models.tag import Tag

import repositories.merchant_repository as merchant_repository
import repositories.tag_repository as tag_repository

merchant_repository.delete_all()
tag_repository.delete_all()

merchant_1 = Merchant('Aldi')
merchant_repository.save(merchant_1)

merchants = merchant_repository.select_all()

for merchant in merchants:
    print(merchant.__dict__)

tag_1 = Tag('Groceries')
tag_repository.save(tag_1)

tags = tag_repository.select_all()

for tag in tags:
    print(tag.__dict__)


pdb.set_trace()