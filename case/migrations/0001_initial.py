# Generated by Django 3.1.2 on 2021-09-24 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestCase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='名称')),
                ('url', models.TextField(verbose_name='URL')),
                ('method', models.CharField(max_length=10, verbose_name='请求方法')),
                ('header', models.TextField(default='{}', null=True, verbose_name='请求头')),
                ('params_type', models.CharField(max_length=10, verbose_name='参数类型')),
                ('params_body', models.TextField(default='{}', null=True, verbose_name='参数内容')),
                ('result', models.TextField(default='{}', null=True, verbose_name='结果')),
                ('assert_type', models.CharField(max_length=10, null=True, verbose_name='断言类型')),
                ('assert_text', models.TextField(default='{}', null=True, verbose_name='结果')),
                ('is_delete', models.BooleanField(default=False, verbose_name='状态')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
        ),
    ]
