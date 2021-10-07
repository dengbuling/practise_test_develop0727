from rest_framework import serializers
from case import models


class AssertData:
    include = "include"
    equal = "equal"


class CaseData:
    methods = ["POST", "GET", "DELETE", "PUT"]
    params_type = ["params", "data", "json"]
    assert_type = [AssertData.include, AssertData.equal]


class CaseSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30, allow_null=False, required=True,
                                 error_messages={
                                     "blank": "请输入性别",
                                     "required": "请输入性别",
                                     "max_length": "性别过长，请重新填写",
                                     "min_length": "性别过短，请重新填写",
                                     "allow_null": "不能为空"
                                 })
    url = serializers.CharField(max_length=50, required=True, error_messages={"required": "请输入性别", })
    method = serializers.ChoiceField(choices=CaseData.methods, error_messages={"invalid_choice": "选择类型错误"})
    params_type = serializers.ChoiceField(choices=CaseData.params_type, error_messages={"invalid_choice": "选择类型错误"},
                                          required=False)
    assert_type = serializers.ChoiceField(choices=CaseData.assert_type, error_messages={"invalid_choice": "选择类型错误"},
                                          required=True)

    header = serializers.JSONField(required=False)

    params_body = serializers.CharField(required=False)
    result = serializers.CharField(required=False)
    assert_text = serializers.CharField(required=False)

    def create(self, validated_data):
        """
        创建用例
        """
        case = models.TestCase.objects.create(**validated_data)
        return case


class CaseValidator(serializers.ModelSerializer):
    class Meta:
        model = models.TestCase
        fields = '__all__'


class DebugValidator(serializers.Serializer):
    """
    用例调试验证器
    """
    url = serializers.CharField(required=True,
                                error_messages={'required': 'URL不能为空'})
    method = serializers.ChoiceField(required=True,
                                     choices=CaseData.methods,
                                     error_messages={'required': 'method不能为空'})
    header = serializers.JSONField(required=True)
    params_type = serializers.ChoiceField(required=True,
                                          choices=CaseData.params_type,
                                          error_messages={'required': 'params_type不能为空'})
    params_body = serializers.JSONField(required=True)


class AssertValidator(serializers.Serializer):
    """
    用例调试验证器
    """
    result = serializers.CharField(required=True, error_messages={'required': 'URL不能为空'})
    assert_type = serializers.ChoiceField(required=True,
                                          choices=CaseData.assert_type,
                                          error_messages={'required': 'method不能为空'})
    assert_text = serializers.CharField(required=True)
