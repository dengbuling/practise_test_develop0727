from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.viewsets import GenericViewSet,ViewSet
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from question import models
import json
import datetime
import uuid
from tools import CreateToken
from tools.LoginAuthentication import TokenAuthentication
from django.db.models import F,Q
from django.shortcuts import render
import os
from rest_framework.versioning import QueryParameterVersioning
from common.Paginator import MyPageNumberPagination, MyPageNumberPagination2
from common.MainView import BaseResponse,BaseView,BaseViewSet
from common.Error import Error
from rest_framework.decorators import action

class LoginSerializer(serializers.ModelSerializer, Error):
    user_name = serializers.CharField(required=True, min_length=2, max_length=20, error_messages=Error.user_msg)
    user_password = serializers.CharField(required=True, min_length=8, max_length=16, error_messages=Error.password_msg)
    user_mobile = serializers.IntegerField(required=True, error_messages=Error.mobile_msg)
    user_gender = serializers.CharField(required=True, error_messages=Error.gender_msg)

    # user_type_name = serializers.CharField(source="user_type")

    # 第二种方式自定义要显示的字段
    # user_1 = serializers.SerializerMethodField()
    #
    # def get_user_1(self, row):
    #     return row.get_user_type_display()


    def create(self, validated_data):
        user_name = validated_data.get("user_name")
        user_password = validated_data.get("user_password")
        user_mobile = validated_data.get("user_mobile")
        user_gender = validated_data.get("user_gender")
        user_type = validated_data.get("user_type")
        create_user = {
            "user_name": user_name,
            "user_password": user_password,
            "user_uuid": uuid.uuid4(),
            "user_mobile": user_mobile,
            "user_gender": user_gender,
        }
        instance = models.User.objects.create(**create_user)
        return instance


    def update(self, instance, validated_data):
        instance.user_name = validated_data.get("user_name")
        instance.user_password = validated_data.get("user_password")
        instance.user_mobile = validated_data.get("user_mobile")
        instance.user_gender = validated_data.get("user_gender")
        instance.save()
        return instance

    class Meta:
        model = models.User

        # model = models.Activity

        # fields = ['user_name', 'user_password', 'user_mobile', 'user_gender', 'user_type_name', 'user_1']
        fields = ['user_name', 'user_password', 'user_mobile', 'user_gender']
        # fields = '__all__'
        # extra_kwargs = {'sex2':{'source':"get_user_type_display"}}

        # 自动序列化，查询所有关联的外键，连表建议<3
        depth = 1



class LoginSerializer2(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'


class Pager(GenericViewSet):
    authentication_classes = []
    permission_classes = []
    queryset = models.User.objects.all().order_by('user_uuid')
    serializer_class = LoginSerializer
    pagination_class = MyPageNumberPagination2

    def list(self, request, *args, **kwargs):
        roles = self.get_queryset()
        pager_roles = self.paginate_queryset(roles)
        ser = self.get_serializer(instance=pager_roles, many=True)
        return Response(ser.data)




class Apple(BaseViewSet):

    authentication_classes = []
    permission_classes = []
    queryset = models.User.objects.all().order_by('user_uuid')
    serializer_class = LoginSerializer


    @action(methods=["get"], detail=False, url_path="list")
    def get_cases_list(self, request, *args, **kwargs):
        print(request.query_params)
        print(kwargs)
        return Response("8888")




class Register(APIView):
    # 单独设置接口不验证token
    authentication_classes = []
    permission_classes = []

    # 验证版本
    versioning_class = QueryParameterVersioning

    def post(self, request, *args, **kwargs):
        username = request.data.get("user_name")
        password = request.data.get("user_password")
        user_mobile = request.data.get("user_mobile")
        user_gender = request.data.get("user_gender")
        aaa = models.User.objects.filter(user_mobile=request.data.get("user_mobile")).first()
        aa = models.User.objects.filter(user_mobile=user_mobile)
        # bb = UserSerializer(instance=aa, many=True)
        payload = {
            "username": aaa.user_name,
            "password": aaa.user_password,
            # "user_type":aaa.user_type,
        }
        user_response = {
            "code": 200,
            "msg": "",
            "token":CreateToken.create_token(payload, 10),
        }
        print(request.query_params.get("version"))
        print(request.version)
        return Response(user_response)


# csrf注释的情况下增加csrf认证
# @method_decorator(csrf_exempt, name='dispatch')
# class Login(APIView,BaseView,Error):
class Login(BaseView, Error):
    # 验证token
    # authentication_classes = [TokenAuthentication, ]
    authentication_classes = []
    # 验证权限
    permission_classes = []

    def get(self, request, *args, **kwargs):

        # 实例化自定义的分页类
        page = MyPageNumberPagination()
        page1 = MyPageNumberPagination2()
        # page2 = MyPageNumberPagination3()

        # 调用方法并传参
        page_data = page.paginate_queryset(queryset=models.User.objects.all(),request=request,view=self)
        page_data1 = page1.paginate_queryset(queryset=models.User.objects.all(),request=request,view=self)

        obj4 = LoginSerializer(instance=page_data, many=True)
        user_response = {
            "code": 200,
            "msg": "",
            "info": obj4.data,
        }
        return Response(user_response)
    # return render(request, 'user/Login.html')

    def post(self, request, *args, **kwargs):
        create_user = {
            "user_name": request.data.get("user_name"),
            "user_password": request.data.get("user_password"),
            "user_uuid": uuid.uuid4(),
            "user_mobile": request.data.get("user_mobile"),
            "user_gender": request.data.get("user_gender"),
        }
        user_response = {
            "code": 200,
            "msg": "",
        }

        """
        data用户传入的参数，通过request.data获取，request.data
        用户传过来的数据先清洗，校验数据合法性
        """

        aaa3 = models.User.objects.all().first()
        # page1 = MyPageNumberPagination()
        # page2 = page1.paginate_queryset(queryset=aaa3,request=request,view=self)
        # print(type(page2))

        # 没有传入instance实例,调用save()时实际上调用了create()
        obj = LoginSerializer(data=request.data)
        # obj22 = LoginSerializer(instance=page2, many=True)
        # print(obj22.data)

        # 在调用对象.data时，要先执行.is_valid()方法后，才能调用
        # obj = LoginSerializer(data=request.data,instance=aaa3)


        # 文件上传
        # try:
        #     file = request.data.get("user_nnn")
        #     file_path = os.path.join('static/file', file.name)
        #     with open(file_path, 'wb') as f:
        #         for chunk in file.chunks():
        #             f.write(chunk)
        #     user_response["file_path"] = file_path
        # except:
        #     user_response["file_path"] = "未上传文件"

        if obj.is_valid():

            create_user["last_modify_time"] = datetime.datetime.now()
            if models.User.objects.filter(user_mobile=request.data.get("user_mobile")):
                models.User.objects.filter(user_mobile=request.data.get("user_mobile")).update(**create_user)
                # obj.save()
                print("7389274892374892")
                user_response["data"] = "用户信息更新成功"

                return Response(user_response)
            else:
                # models.User.objects.create(**create_user)
                obj.save()
                user_response["data"] = "用户信息注册成功"
                return Response(user_response)
        else:
            user_response["code"] = 500
            user_response["msg"] = "数据填写错误"
            user_response["data"] = obj.errors
            print(user_response)

            print(self.response(error=self.PROJECT_ID_NULL))
            print(self.PROJECT_ID_NULL)
            print(type(self.PROJECT_ID_NULL))
            return self.response(data=obj.errors)
            # return Response(user_response)
            # print(obj.errors["user_name"][0])
            # return render(request, 'user/Login.html', {'user_response': user_response})


    def put(self, request, *args, **kwargs):
        create_user = {
            "user_name": request.data.get("user_name"),
            "user_password": request.data.get("user_password"),
            "user_uuid": uuid.uuid4(),
            "user_mobile": request.data.get("user_mobile"),
            "user_gender": request.data.get("user_gender"),
        }
        user_response = {
            "code": 200,
            "msg": "",
        }

        # 传入instance实例时调用update()方法,无实例传入时调用的是create()方法
        obj = LoginSerializer(data=request.data,instance=models.User.objects.filter(user_mobile=request.data.get("user_mobile")).first())
        if obj.is_valid():
            obj.save()
            user_response["data"] = "用户信息更新成功"
            return Response(user_response)
        else:
            user_response["code"] = 500
            user_response["msg"] = "数据填写错误"
            user_response["data"] = obj.errors
            print(user_response)
            return Response(user_response)


class Question(APIView):
    # 验证token
    # authentication_classes = [TokenAuthentication, ]
    authentication_classes = []

    def post(self, request, *args, **kwargs):
        create_question = {
            "question_name": request.data.get("question_name"),
        }
        user_response = {
            "code": 200,
            "msg": "",
        }
        if models.Question.objects.filter(question_name=request.data.get("question_name")):
            user_response["data"] = "问题创建失败，问题已存在，请创建新问题"
            return Response(user_response)
        else:
            models.Question.objects.create(**create_question)
            user_response["data"] = "问题创建成功"
            return Response(user_response)


class Choice(APIView):
    # 验证token
    # authentication_classes = [TokenAuthentication, ]
    authentication_classes = []

    def post(self, request, *args, **kwargs):

        question_list = models.Question.objects.filter(question_name=request.data.get("question_name")).first()
        question_reverse = question_list.choice_set.all()
        create_choice = {
            "choice_name": request.data.get("choice_name"),
            "question_choice_id": question_list.id,
        }
        user_response = {
            "code": 200,
            "msg": "",
        }
        if request.data.get("choice_name") in [index.choice_name for index in question_reverse]:
            user_response["data"] = "答案创建失败，该问题下答案已存在，请创建新答案"
            return Response(user_response)
        else:
            models.Choice.objects.create(**create_choice)
            user_response["data"] = "答案创建成功"
            return Response(user_response)


class Activity(APIView):
    # 验证token
    # authentication_classes = [TokenAuthentication, ]
    authentication_classes = []

    def post(self, request, *args, **kwargs):
        question_list = models.Question.objects.filter(question_name=request.data.get("question_name")).first()
        choice_list = models.Choice.objects.filter(choice_name=request.data.get("choice_name")).first()
        activity_creator = models.User.objects.filter(user_mobile=request.data.get("mobile")).first()
        activity_creator_uuid = activity_creator.user_uuid
        activity_list = models.Activity.objects.filter(activity_creator=activity_creator_uuid)
        create_activity = {
            "activity_name": request.data.get("activity_name"),
            "activity_creator_id": activity_creator_uuid,
            "question_id_id": question_list.id,
            "choice_id_id": choice_list.id,
            "activity_id": uuid.uuid4(),
        }
        user_response = {
            "code": 200,
            "msg": "",
        }
        # aaa = models.Question.objects.filter(pk=1).first()
        # bbb = aaa.question_reverse.all()
        # for i in bbb:
        #     print(i.choice_id.choice_name)
        # return Response("99")
        if request.data.get("activity_name") in [index.activity_name for index in activity_list]:
            user_response["data"] = "活动创建失败，该活动已存在，请创建新活动"
            return Response(user_response)
        else:
            models.Activity.objects.create(**create_activity)
            user_response["data"] = "活动创建成功"
            return Response(user_response)



# class Register2(APIView):
#     # 单独设置接口不验证token
#     authentication_classes = []
#
#     def get(self, request, *args, **kwargs):
#         pass
#
#     def post(self, request, *args, **kwargs):
#         username = request.data.get("username")
#         password = request.data.get("password")
#         user_uuid = uuid.uuid4()
#         user_mobile = request.data.get("mobile")
#         user_gender = request.data.get("gender")
#         # User.objects.create(user_name=username,user_uuid=user_uuid,user_password=password,user_mobile=user_mobile,user_gender=user_gender,)
#         aaa = User.objects.filter(user_mobile=user_mobile).first()
#         aa = User.objects.filter(user_mobile=user_mobile)
#         # bb = UserSerializer(instance=aa, many=True)
#
#         # 通过外键question_choice正向跨表查询
#         choice_1 = models.Choice.objects.filter(pk=2).first()
#         # 取值时跨表
#         question_1 = choice_1.question_choice.question_name
#         # print(question_1)
#
#         # 通过外键question_choice正向查询，内部元素是字典
#         # question_choice_id是因为隐含生成_id；question_choice__question_name双下划线跨表查询
#         # 查询时跨表
#         question_2 = models.Choice.objects.all()[0:4].values('choice_name', 'question_choice_id',
#                                                              'question_choice__question_name')
#         # print(question_2)
#
#         # 通过外键question_choice正向查询，内部元素是元祖
#         question_3 = models.Choice.objects.all()[0:4].values_list('choice_name', 'question_choice_id',
#                                                                   'question_choice__question_name')
#         # print(question_3)
#
#         # 通过小写表名_set.all()反向跨表查询
#         question_4 = models.Question.objects.filter(pk=2).first()
#         # 取值时跨表
#         choice_4 = question_4.choice_set.all()
#         # print(choice_4)
#
#         # 通过小写表名反向跨表查询，类似Mysql的left join
#         question_5 = models.Question.objects.all().values('question_name', 'choice')
#         # print(question_5)
#         question_6 = models.Question.objects.all().values('question_name', 'choice__choice_name')
#         # print(question_6)
#         # print(question_6.query)
#
#         # 根据pk升序排序
#         choice_6 = models.Choice.objects.all().order_by('pk')
#         # print(choice_6)
#         # 根据pk降序排序
#         choice_7 = models.Choice.objects.all().order_by('-pk')
#         # print(choice_7)
#
#         # 更新表choice，将choice_delete+1
#         # models.Choice.objects.filter(pk=1).update(choice_delete=F('choice_delete')+1)
#
#         # 补充执行sql语句
#         choice_8 = models.Choice.objects.all().extra(
#             select={'m': "select modify_time from question WHERE id=%s"},
#             select_params=[1, ],
#             tables=['question'],
#             where=['choice.question_choice_id=question.id'],
#             # params=[None, ],
#             order_by=['-choice.id'],
#         )
#         # print(choice_8)
#         # print(choice_8.query)
#
#         # 执行原生sql
#         cursor = connection.cursor()  # cursor = connections['default'].cursor()
#         cursor.execute(
#             """SELECT question.id,question.question_name,choice.choice_name,choice.question_choice_id from question LEFT JOIN choice ON question.id = choice.question_choice_id""")
#         row = cursor.fetchall()
#         # print(row)
#
#         # sql查询优化
#         choice_9 = models.Choice.objects.all().prefetch_related('question_choice')
#         # choice_9 = models.Choice.objects.all().select_related('question_choice')
#         # print(choice_9)
#         print(choice_9.query)
#
#         # sql查询优化
#         choice_10 = models.Choice.objects.filter(question_choice__question_name='Python是不是最好的编程语言？').select_related(
#             'question_choice')
#         print(choice_10)
#         print(choice_10.query)
#
#         # 获取请求中的内容
#         # page = request.query_params.get("page")
#         # print(page)
#
#         payload = {
#             "username": aaa.user_name,
#             "password": aaa.user_password,
#         }
#         ee = {
#             # "data": bb.data,
#             "token": CreateToken.create_token(payload, 1),  # 生成token，过期时间5分钟
#             "status": 200,
#             "msg": "success!"
#         }
#         # return Response(bb.data)
#         return JsonResponse(ee, json_dumps_params={"ensure_ascii": False})
        # return JsonResponse(ee, json_dumps_params={"ensure_ascii": False})
