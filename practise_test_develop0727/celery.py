import os
from celery import Celery

# 配置文件位置
os.environ.setdefault('DJANGO_SETTINGS_MODULE','practise_test_develop0727.settings')

# 传参项目名称
app = Celery('practise_test_develop0727')

app.config_from_object('django.conf:settings',namespace='CELERY')

# 去每个已注册的APP中读取task.py文件
app.autodiscover_tasks()