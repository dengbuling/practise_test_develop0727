import time
from celery import Celery

app = Celery("tasks", broker="redis://localhost:6379", backend="redis://localhost:6379")


@app.task
def x1(x, y):
    time.sleep(5)
    return x + y


@app.task
def x2(x, y):
    time.sleep(5)
    return x - y
