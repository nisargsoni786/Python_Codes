from tasks import add
from celery.result import AsyncResult

res=(add.delay(4,3))

# print(res)
