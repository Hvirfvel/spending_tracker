import pdb
from models.merchant import Merchant

import repositories.merchant_repository as merchant_repository

merchant_repository.delete_all()

merchant_1 = Merchant("Aldi")
merchant_repository.save(merchant_1)

merchants = merchant_repository.select_all()

for merchant in merchants:
    print(merchant.__dict__)


pdb.set_trace()