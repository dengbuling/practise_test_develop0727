from django.db import models


# Create your models here.

class Question(models.Model):
    question_group = (
        (1, 'question'),
        (2, 'time'),
        (3, 'stats'),
    )

    question_name = models.CharField(max_length=20)
    question_delete = models.IntegerField(default=0)
    question_category = models.IntegerField(null=True, default=1)
    create_time = models.DateTimeField(auto_now_add=True)
    last_modify_time = models.DateTimeField(auto_now=True)

    # 唯一索引，只能有一个question_name
    # question_name = models.CharField(max_length=20,unique=True)

    # pycharm对django代码objects无代码提示问题的解决方案
    objects = models.Manager()

    # 增加默认标签
    def __str__(self):
        return self.question_name

    class Meta:
        db_table = "question"


class Choice(models.Model):
    choice_name = models.CharField(max_length=20)
    choice_delete = models.IntegerField(default=0)
    create_time = models.DateTimeField(auto_now_add=True)
    last_modify_time = models.DateTimeField(auto_now=True)
    question_choice = models.ForeignKey("Question", on_delete=models.CASCADE)

    # pycharm对django代码objects无代码提示问题的解决方案
    objects = models.Manager()

    # 增加默认标签
    def __str__(self):
        return f'{self.pk},{self.choice_name}'

    class Meta:
        db_table = "choice"


class Activity(models.Model):
    activity_id = models.UUIDField(primary_key=True)
    activity_name = models.CharField(max_length=32)
    # to_field = 'id'设置默认关联哪个字段
    question_id = models.ForeignKey("Question", db_column="question", on_delete=models.CASCADE,
                                    related_name="question_reverse")
    choice_id = models.ForeignKey("Choice", db_column="choice", on_delete=models.CASCADE, related_name="choice_reverse")
    activity_creator = models.ForeignKey("User", to_field="user_uuid", on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)
    last_modify_time = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    def __str__(self):
        return self.activity_name


    class Meta:
        db_table = 'activity'


# 用户表
class User(models.Model):
    gender_choice = {
        (1, "男"),
        (2, "女"),
        (3, "保密")
    }
    user_type_choice = {
        (1, "普通用户"),
        (2, "银卡会员"),
        (3, "金卡会员"),
        (4, "白金卡会员"),
        (5, "钻石卡会员"),
    }
    user_name = models.CharField(max_length=50, unique=True)
    user_password = models.CharField(max_length=20)
    user_uuid = models.CharField(primary_key=True, unique=True, max_length=64)
    user_mobile = models.CharField(max_length=20, unique=True)
    user_gender = models.CharField(max_length=2, choices=gender_choice)
    user_isDelete = models.IntegerField(default=0)
    crete_time = models.DateTimeField(auto_now=True)
    last_modify_time = models.DateTimeField(auto_now_add=True)

    user_type = models.IntegerField(choices=user_type_choice, default=2)

    # pycharm对django代码objects无代码提示问题的解决方案
    objects = models.Manager()

    def __str__(self):
        return self.user_name

    class Meta:
        db_table = "Base_user"

