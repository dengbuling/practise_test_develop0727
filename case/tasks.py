import time
from celery import shared_task
from tools.SMS_context import send_sms_single
import random


@shared_task
def x1(x, y):
    time.sleep(5)
    return x + y


@shared_task
def x2(x, y):
    time.sleep(5)
    return x - y


@shared_task
def x3(x, y):
    code = random.randrange(1000, 9999)
    res = send_sms_single(x, y, [code, 3, ])
    return res
