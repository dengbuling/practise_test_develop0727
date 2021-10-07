from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework.pagination import CursorPagination


class MyPageNumberPagination(PageNumberPagination):
    """
    自定义分页
    """
    # 默认页码
    page = 3
    # 默认每页显示多少条数据
    page_size = None
    # 每页最多显示多少条数据
    max_page_size = 4
    # 每页显示多少条数据
    page_size_query_param = 'size'
    # 当前页码
    page_query_param = 'page'


class MyPageNumberPagination2(LimitOffsetPagination):
    """
    自定义分页
    """
    # 默认往后取几位
    default_limit = 3
    # 要取得第一个数据的id
    offset_query_param = 'offset'
    # 往后取几位
    limit_query_param = 'limit'
    # 最多取几条数据
    max_limit = 5

# class MyPageNumberPagination3(CursorPagination):
#     cursor_query_param = 'cursor'
#     page_size = 2
#     ordering = '-user_mobile,,'
#     page_size_query_param = 'size'
#     max_page_size = 5
