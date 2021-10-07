# Generated by Django 3.1.2 on 2021-09-18 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0007_auto_20210917_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_gender',
            field=models.CharField(choices=[(1, '男'), (2, '女'), (3, '保密')], max_length=2),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.IntegerField(choices=[(5, '钻石卡会员'), (3, '金卡会员'), (1, '普通用户'), (4, '白金卡会员'), (2, '银卡会员')], default=2),
        ),
    ]
