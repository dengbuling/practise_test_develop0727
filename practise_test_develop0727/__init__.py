import pymysql

# django程序没有自动运行celery文件，需要手动导入运行
from .celery import app as celery_app

# 指定mysql版本
pymysql.version_info = (1, 4, 13, "final", 0)

pymysql.install_as_MySQLdb()

__all__ = ('celery_app',)
