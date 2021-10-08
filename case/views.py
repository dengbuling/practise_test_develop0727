from common.MainView import BaseViewSet
from rest_framework.decorators import action
from case.serializer import CaseSerializer, CaseValidator,DebugValidator,AssertValidator,AssertData
from case import models,tasks
from common.Paginator import MyPageNumberPagination
import requests
import json
import os
from common.TestCase import UnittestCase
from celery.result import AsyncResult
from practise_test_develop0727 import celery_app
import datetime
from django import forms
from django.shortcuts import render
from question.models import User
from tools.SMS_context import send_sms_single


class CaseForm(forms.ModelForm):
    user_name = forms.CharField(label="用户名")
    # 设置密码密文输入
    user_password = forms.CharField(label="密码", widget=forms.PasswordInput())
    confirm_password = forms.CharField(label="确认密码", widget=forms.PasswordInput())
    code = forms.CharField(label="验证码")
    user_mobile = forms.CharField(label="手机号")

    class Meta:
        model = User
        fields = ['user_name', 'user_password', 'confirm_password', 'user_mobile', 'code']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 获取字段名称和字段名称后面的对象
        for name, field in self.fields.items():
            field.widget.attrs["class"] = 'form-control'
            field.widget.attrs["placeholder"] = f'请输入{field.label}'


class TestCase(BaseViewSet):
    authentication_classes = []
    permission_classes = []
    queryset = models.TestCase.objects.all()
    pagination_class = MyPageNumberPagination()

    @action(methods=["post"], detail=False, url_path="create")
    def get_cases_list(self, request, *args, **kwargs):
        aaa = CaseSerializer(data=request.data)
        if aaa.is_valid():
            aaa.save()
            return self.response(data=aaa.data)
        else:
            return self.response(error=aaa.errors)

    @action(methods=["get"], detail=False, url_path="look")
    def get_cases_list2(self, request, *args, **kwargs):
        page_num = request.query_params.get("page", 1)
        size_num = request.query_params.get("size", 1)
        bbb = models.TestCase.objects.all()
        pager = MyPageNumberPagination()
        pager2 = pager.paginate_queryset(queryset=self.queryset, request=request, view=self)
        pager3 = self.pagination_class.paginate_queryset(queryset=self.queryset, request=request, view=self)
        try:
            aaa = CaseValidator(instance=pager2, many=True)
        except:
            return self.response(error=self.CASE_ID_NULL)
        data = {
            "count": models.TestCase.objects.all().count(),
            "page": int(page_num),
            "size": int(size_num),
            "list": aaa.data,
        }
        return self.response(data=data)


    @action(methods=["post"], detail=False, url_path="debug")
    def debug_cases(self, request, *args, **kwargs):
        aaa = DebugValidator(data=request.data)
        if not aaa.is_valid():
            return self.response(error=aaa.errors)

        url = request.data.get("url")
        method = request.data.get("method")
        header = request.data.get("header")
        params_type = request.data.get("params_type")
        params_body = request.data.get("params_body")
        result_text = None
        # payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
        if method == "GET":
            result_text = requests.get(url,params=params_body)
        if method == "POST":
            result_text = requests.post(url, data=params_body)
        print(result_text)
        print(params_body)
        print(type(result_text))
        a444 = result_text.json()
        print(a444["headers"]["Host"])
        print(a444)
        return self.response(data=result_text)


    @action(methods=["post"], detail=False, url_path="assert")
    def assert_cases(self, request, *args, **kwargs):
        aaa = AssertValidator(data=request.data)
        if not aaa.is_valid():
            return self.response(error=aaa.errors)
        result = request.data.get("result")
        assert_type = request.data.get("assert_type")
        assert_text = request.data.get("assert_text")


        method = request.data.get("method")
        url = request.data.get("url")
        params_body = request.data.get("params_body")

        result_text = None
        if method == "GET":
            result_text = requests.get(url,params=params_body)
        if method == "POST":
            result_text = requests.post(url, data=params_body)
        a444 = result_text.json()
        a555 = a444["headers"]["Host"]
        print(a555)


        asa = aaa.data
        if assert_type == AssertData.equal:
            if a555 == assert_text:
                asa["message2"] = "断言成功"
                print("断言成功")
                return self.response(data=asa)
            else:
                asa["mee2"] = "断言失败"
                print("断言失败")
                return self.response(data=asa)
        elif assert_type == AssertData.include:
            if assert_text in result:
                asa["message2"] = "断言成功"
                return self.response(data=asa)
            else:
                asa["message2"] = "断言失败"
                return self.response(data=asa)

        return self.response(data=aaa.data)



    @action(methods=["get"], detail=False, url_path="unittest")
    def unittest_cases(self, request, *args, **kwargs):
        UnittestCase.main()
        return self.response(data="success")

    @action(methods=["get"], detail=False, url_path="task")
    def task_cases(self, request, *args, **kwargs):
        # 立即执行
        result = tasks.x1.delay(2, 2)
        # 任务队列发送短信
        # tasks.x3.delay('18642662530', 1149390)
        return self.response(data=result.id)

    @action(methods=["get"], detail=False, url_path="tasktime")
    def tasktime_cases(self, request, *args, **kwargs):
        ntime = datetime.datetime.now()
        utctime = datetime.datetime.utcnow()
        # 本地时间转换为utc时间
        cctime = datetime.datetime.utcfromtimestamp(ntime.timestamp())
        targettime = utctime + datetime.timedelta(seconds=5)
        # 定时执行定时任务
        print(targettime)
        result = tasks.x1.apply_async(args=[2, 2], eta=targettime)
        # 定时任务发送短信
        # tasks.x3.apply_async(args=['18642662530', 1149390], eta=targettime)
        return self.response(data=result.id)



    @action(methods=["get"], detail=False, url_path="backend")
    def backend_case(self, request, *args, **kwargs):
        aid = request.query_params.get('aid')
        result1 = AsyncResult(aid, app=celery_app)
        # 获取状态
        print(result1.status)
        # 获取数据
        print(result1.get())
        # 遗忘数据
        # result1.forget()
        # 停止定时任务git config --system --unset credential.helper
        # result1.revoke()
        # 一般情况下
        # 如果执行成功
        # if result1.successful():
        #     result1.get()
        #     result1.forget()
        # elif result1.failed():
        #     pass
        return self.response(data=result1.get())

    @action(methods=["get"], detail=False, url_path="register")
    def register(self, request, *args, **kwargs):
        form = CaseForm()
        return render(request, 'case/register.html', {'form': form})

    @action(methods=["get"], detail=False, url_path="message")
    def message(self, request, *args, **kwargs):
        import random
        code = random.randrange(1000,9999)
        res = send_sms_single('1864266253',1149390,[code,3,])
        print(res)
        if res['result'] == 0:
            return self.response(data=res['errmsg'])
        else:
            return self.response(data=res['errmsg'])
