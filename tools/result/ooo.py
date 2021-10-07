from celery.result import AsyncResult
from yyy import app

result1 = AsyncResult("9a7df53d-7a72-4922-ae4c-113405932f4e",app=app)

print(result1.status)
print(result1.get())