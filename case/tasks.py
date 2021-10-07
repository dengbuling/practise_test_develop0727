import time
from celery import shared_task


@shared_task
def x1(x, y):
    time.sleep(5)
    return x + y


@shared_task
def x2(x, y):
    time.sleep(5)
    return x - y
