class Error:
    """
    子定义错误码与错误信息
    """
    USER_OR_PAWD_NULL = {"10010": "用户名密码为空"}
    USER_OR_PAWD_ERROR = {"10011": "用户名密码错误"}

    user_msg = {
        "blank": "请输入用户名",
        "required": "请输入用户名",
        "max_length": "用户名过长，请重新填写",
        "min_length": "用户名过短，请重新填写"
    }

    password_msg = {
        "blank": "请输入密码",
        "required": "请输入密码",
        "max_length": "密码过长，请重新填写",
        "min_length": "密码过短，请重新填写"
    }
    mobile_msg = {
        "blank": "请输入手机号",
        "required": "请输入手机号",
        "max_length": "手机号过长，请重新填写",
        "min_length": "手机号过短，请重新填写"
    }
    gender_msg = {
        "blank": "请输入性别",
        "required": "请输入性别",
        "max_length": "性别过长，请重新填写",
        "min_length": "性别过短，请重新填写"
    }


    ParamsTypeError = {"30020": "参数类型错误"}
    JSON_TYPE_ERROR = {"30030": "JSON格式错误"}

    USER_ID_NULL = {"40010": "用户id不存在"}

    PROJECT_ID_NULL = {"10020": "项目id不存在"}
    PROJECT_OBJECT_NULL = {"10021": "通过id查询项目不存在"}
    PROJECT_DELETE_ERROR = {"10023": "项目删除失败"}

    MODULE_ID_NULL = {"10030": "模块id不存在"}
    MODULE_OBJECT_NULL = {"10031": "模块对象不存在"}
    MODULE_DELETE_ERROR = {"10032": "模块删除失败"}

    CASE_ID_NULL = {"10040": "用例id不存在"}
    CASE_OBJECT_NULL = {"10041": "通过id查询用例不存在"}
    CASE_HEADER_ERROR = {"10042": "header类型错误，不是json"}
    CASE_PARAMS_BODY_ERROR = {"10043": "params_body类型错误，不是json"}
    ASSERT_INCLUDE_FAIL = {"10044": "断言包含失败"}
    ASSERT_EQUAL_FAIL = {"10045": "断言相等失败"}


class Error123:
    def __init__(self, arg):
        self.arg = arg

    def user_error(self):
        msg = {
            "blank": f"请输入{self.arg}",
            "required": f"请输入{self.arg}",
            "max_length": f"{self.arg}过长，请重新填写",
            "min_length": f"{self.arg}过短，请重新填写"
        }
        return msg
