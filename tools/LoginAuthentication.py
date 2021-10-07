import jwt
from django.conf import settings
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed


class TokenAuthentication(BaseAuthentication):

    def authenticate(self, request):
        token = request.data.get("token")
        salt = settings.SECRET_KEY
        try:
            payload = jwt.decode(token, salt, algorithms=['HS256'])
            print("请求成功")
        except jwt.exceptions.ExpiredSignatureError:
            print("token已失效")
            raise AuthenticationFailed({"code": 1002, "message": "token已失效"})
        except jwt.DecodeError:
            print("token认证失败")
            raise AuthenticationFailed({"code": 1003, "message": "token认证失败"})
        except jwt.InvalidTokenError:
            print("非法请求")
            raise AuthenticationFailed({"code": 1004, "message": "非法请求"})

        # 抛出异常，后续不再执行
        # return返回一个元组，表示认证通过。request.user就是元组第一个值，request.auth就是元组第二个值
        return (payload, token)
