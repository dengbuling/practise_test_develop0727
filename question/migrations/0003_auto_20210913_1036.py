# Generated by Django 3.1.2 on 2021-09-13 10:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0002_auto_20210912_0236'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='modify_time',
            new_name='last_modify_time',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='modify_time',
            new_name='last_modify_time',
        ),
        migrations.RemoveField(
            model_name='question',
            name='question_555u',
        ),
        migrations.RemoveField(
            model_name='question',
            name='question_kk',
        ),
        migrations.AlterField(
            model_name='question',
            name='question_category',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_gender',
            field=models.CharField(choices=[(3, '保密'), (1, '男'), (2, '女')], max_length=2),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_password',
            field=models.CharField(max_length=20),
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('create_time', models.DateTimeField(auto_created=True)),
                ('activity_id', models.UUIDField(primary_key=True, serialize=False)),
                ('activity_name', models.CharField(max_length=32)),
                ('last_modify_time', models.DateTimeField(auto_now=True)),
                ('activity_creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question.user')),
                ('choice_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choice_reverse', to='question.choice')),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_reverse', to='question.question')),
            ],
            options={
                'db_table': 'activity',
            },
        ),
    ]
