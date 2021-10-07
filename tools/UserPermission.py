from question import models
from rest_framework.permissions import BasePermission


class UserPermission(BasePermission):
    message = "必须是会员才能访问"

    def has_permission(self, request, view):
        vip = models.User.objects.filter(user_name=request.user["username"]).first().user_type
        if int(vip) != 2:
            return False
        return True
