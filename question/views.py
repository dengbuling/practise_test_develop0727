from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,QueryDict
from .models import Question,Choice
from django.views import View
import time,datetime
from rest_framework import serializers
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
import json
from rest_framework.response import Response
import uuid




# Create your views here.


# 自定义验证规则
class RoleValidator(object):

    def __init__(self, base):
        # base表示"老男人"
        self.base = base

    def __call__(self, value):
        # value表示提交过来的值，如果提交过来的值不是以"老男人"开头
        if not value.startswith(self.base):
            message = f'标题必须以{self.base}开头'
            raise serializers.ValidationError(message)

    def set_context(self, serializer_field):
        """
        This hook is called by the serializer instance,
        prior to the validation call being made.
        """
        # 执行验证之前调用,serializer_fields是当前字段对象
        pass

# 自定义序列化类
class QuestionSerializer(serializers.Serializer):

    question_name = serializers.CharField(validators=[RoleValidator("今年"), ],required=True)

    # 第一种方式获取question_category choice要显示的内容
    # question_category2 = serializers.CharField(source="get_question_category_display")

    # 第二种方式获取question_category choice要显示的内容
    question_category3 = serializers.SerializerMethodField()

    def get_question_category3(self, obj):
        return obj.get_question_category_display()


# 序列化类
class QuestionModelSerializer(serializers.ModelSerializer):
    question_name = serializers.CharField(validators=[RoleValidator("老男人"), ])
    question_category2 = serializers.CharField(source="get_question_category_display")
    create_time = serializers.DateTimeField(format="%y-%m-%d %H:%M:%S")
    modify_time = serializers.DateTimeField(format="%y-%m-%d %H:%M:%S")

    question_category3 = serializers.SerializerMethodField()

    def get_question_category3(self, obj):
        return obj.get_question_category_display()

    class Meta:
        model = Question
        fields = '__all__'


class ChoiceSerializer(serializers.ModelSerializer):
    # 通过外键question_choice找到question表中的question_name
    choice_ForeignKey_question = serializers.CharField(source="question_choice.question_name")

    # 显示choice表中的所有字段
    class Meta:
        model = Choice
        fields = '__all__'


class MyBaseView(object):
    def dispatch(self, request, *args, **kwargs):
        # 继承Home的父类View里面的dispatch
        rec = super().dispatch(request, *args, **kwargs)
        # print("get")
        return rec


class HomeView(APIView):
    def post(self, request, *args, **kwargs):

        QN = request.data.get("question_name")
        QD = request.data.get("id")

        a = Question.objects.filter(pk=5)
        a1 = Question.objects.filter(question_name=QN,id=QD).first()
        # b = QuestionModelSerializer(instance=a, many=True)
        # g = json.dumps(a1.data,ensure_ascii=False)
        print(type(a1))
        print(type(a))
        print(a1)

        # b = QuestionSerializer(instance=a, many=True)
        b = QuestionModelSerializer(instance=a, many=True)
        # print(a)
        c = QuestionSerializer(data=request.data)
        salt = "64721yurewbfkjweri32yi28y2f"
        kkk = datetime.datetime.utcnow()+datetime.timedelta(minutes=3)
        aaaa = {
            "id": a1.id,
            "question_name": a1.question_name,
            "exp": datetime.datetime.now() + datetime.timedelta(minutes=5) # 超时时间
        }
        print(kkk)
        print(aaaa)

        if c.is_valid():
            print(c.validated_data)
            # print(request.data)

            for i in b.data:
                i["request.path"] = request.path
                i["request.method"] = request.method
                # i["UUID"] = uuid.uuid4()
            e = {
                "code": 200,
                "msg": "success!",
                "data": b.data,
            }

            token = jwt.encode(payload=aaaa, key=salt, algorithm="HS256")
            print(token)
            # f = {
            #     "code": 200,
            #     "msg": "success!",
            #     "data": b.data,
            #     "token":token,
            # }
            return JsonResponse(e, json_dumps_params={'ensure_ascii': False})
            # return Response(e)
        else:
            print(c.errors)
            f = {
                "code": 10086,
                "msg": "参数不合法!",
                "data": c.errors
            }
            return JsonResponse(f, json_dumps_params={'ensure_ascii': False})



# csrf认证装饰器
@method_decorator(csrf_exempt, name='dispatch')
class Home(View):

    def get(self, request, *args, **kwargs):
        a = Choice.objects.all()[0:2]
        b = ChoiceSerializer(instance=a, many=True)
        c = {
            "code": 200,
            "msg": "success!",
            "data": b.data
        }
        return JsonResponse(c, json_dumps_params={'ensure_ascii': False})

    def post(self, request, *args, **kwargs):
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        print(username)
        print(password)
        a = Choice.objects.all()[0:2]
        b = ChoiceSerializer(instance=a, many=True)
        c = {"username": username, "password": password}
        d = json.dumps(c, ensure_ascii=False)
        # 拿到请求参数
        # e = json.loads(request.body)
        # if e["question_name"] == "老男人8":
        #     print("Good")
        return HttpResponse(d)










def practise_1(request):
    dic = {"question_name":"手机号是?","question_delete":0}
    #Question.objects.create(question_name="今年几岁了？",question_delete=0)
    #Question.objects.create(**dic)

    #Question.objects.create(**dic)
    #Question.objects.filter(pk=9).update(question_name="姓名是？",modify_time=time.strftime("%Y-%m-%d %H:%M:%S"))
    #Question.objects.filter(pk=9).delete()

    question_serializer = QuestionSerializer(data={'question_name': 'Python是不是最好的编程语言？', 'question_delete': 1})
    question_serializer.is_valid()
    question_serializer.save()
    print(question_serializer.is_valid(), question_serializer.data)


    return HttpResponse(question_serializer)


def practise_2(request):
    dic = {"question_name":"手机号是?","question_delete":0}
    #Question.objects.create(question_name="今年几岁了？",question_delete=0)
    #Question.objects.create(**dic)

    #Question.objects.create(**dic)

    # 更新数据库
    #Question.objects.filter(pk=9).update(question_name="姓名是？",modify_time=time.strftime("%Y-%m-%d %H:%M:%S"))

    #aa = Question.objects.filter(question_name__contains="几岁")

    # 反向查询
    # choice_set为小写（首字母和中间的都要小写）
    # obj是使用.get（）获取的单一查询 ，使用filter（），excute（）等获取的是查询集集合不能用此方法
    Question.objects.get(pk=1).choice_set.create(choice_name="今年几岁了？",choice_delete=0,create_time=datetime.now().strftime("%Y-%m-%d %X"))

    # 反向查询
    bb = Question.objects.get(pk=1).choice_set.all()
    print(bb)


    return render(request, 'question/Login.html', {'question': bb})
    # return HttpResponse(bb)

