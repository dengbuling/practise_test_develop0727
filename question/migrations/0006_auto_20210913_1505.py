# Generated by Django 3.1.2 on 2021-09-13 15:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0005_auto_20210913_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='choice_id',
            field=models.ForeignKey(db_column='choice', on_delete=django.db.models.deletion.CASCADE, related_name='choice_reverse', to='question.choice'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='question_id',
            field=models.ForeignKey(db_column='question', on_delete=django.db.models.deletion.CASCADE, related_name='question_reverse', to='question.question'),
        ),
        migrations.AlterField(
            model_name='choice',
            name='choice_delete',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='choice',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_category',
            field=models.IntegerField(default=1, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_delete',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_gender',
            field=models.CharField(choices=[(3, '保密'), (1, '男'), (2, '女')], max_length=2),
        ),
    ]