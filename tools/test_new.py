from types import MethodType, FunctionType


# class A(object):
#     def __init__(self, aa):
#         self.a1 = aa
#
#     def __new__(cls, *args, **kwargs):
#         return "999"
#
#     def __call__(self, value):
#         print(value)
#
#
# a = A()
# a("888")

# aa = "11000101"
# print(int(aa, base=2))
#
# bb = {
#     "yy": "767",
#     "uu": "453",
#     "ii": "000"
# }
#
#
# print(bb.get("ll"))


# class MM(object):
#     def __init__(self,name):
#         self.name = name
#
#     def __call__(self, *args, **kwargs):
#         print("999")
#
#     @property
#     def ll(self):
#         print("property")
#
#     @staticmethod
#     def gg():
#         print("static")
#
#     @classmethod
#     def kk(cls):
#         print("class")
# MM.kk()
# MM.gg()
# pp=MM("uu")
# pp()
# print(isinstance(MM.kk,MethodType))
# print(pp.gg)


# class NN(object):
#     # def __init__(self):
#     #     self.ll = []
#
#     ll = []
#     #print(ll)
#     def list(self):
#         self.ll.insert(0, 33)
#         return self.ll
#
#
# qq = NN()
# ww = NN()
#
# rr = qq.list()
#
#
#
# print(rr)
#
# tt = ww.list()
# print(tt)


# class Base(object):
#
#     def __new__(self):
#         pass
#
#     def __init__(self):
#         pass
#
#     def __call__(self, *args, **kwargs):
#         pass
#
#     def __str__(self):
#         pass
#
#     def __enter__(self):
#         pass
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         pass
#
#     def


# class Foo:
#     f = '类的静态变量'
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def say_hi(self):
#         print('hi,%s'%self.name)
# obj=Foo('egon',73)
# #检测是否含有某属性
# print(hasattr(obj,'name'))
# print(hasattr(obj,'say_hi'))
# #获取属性
# n=getattr(obj,'name')
# print(n)
# func=getattr(obj,'say_hi')
# func()


# bb = {
#     "yy": "767",
#     "uu": "453",
#     "ii": "000"
# }
# for i in enumerate(bb,1):
#     print(i)


class FF(object):
    def send(self):
        raise NotImplementedError("必须重写")


class LL(FF):
    # def pp(self):
    #     pass
    pass


# h = FF()
# h.pp()

# g = LL()
# g.send()

import hashlib

import logging

# from collections import Iterable
# from collections import Iterator

salt = "fhdkjhfehjkse5nfdsk".encode('utf-8')
obj = hashlib.md5(salt)
obj.update("fhdjshfkjs".encode('utf-8'))
pp = obj.hexdigest()
print(pp)

salt = "93849038490384902".encode('utf8')
w2 = 'hdjshdjkahdkjsh'.encode()
w1 = hashlib.md5(salt)
w1.update(w2)
print(w1.hexdigest())

logger = logging.basicConfig(filename="fhdjks.log", level=logging.INFO,
                             format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logging.info("Start print log")
logging.debug("Do something")
logging.warning("Something maybe fail.")
logging.info("Finish")

# def func():
#     print("呵呵")
#     print(func)
# a = func    # 把函数当成一个值赋值给另一个变量
# a()     # 函数调用 func()

r1 = [1, 2, 3, 4, 5]
print(dir(r1))

r2 = r1.__iter__()
print(hasattr(r2, '__next__'))
# print(isinstance(r2,Iterator))
while True:
    try:
        print(r2.__next__())
    except StopIteration:
        break

# def eat():
#     for i in range(1,10000):
#         yield '包子'+str(i)
# e = eat()
# print(e.__next__())
# print(e.__next__())
# print(e.__next__())
# print(e.__next__())
# print(e.__next__())
# print(e.__next__())
# print(e.__next__())
#
#
# def eat():
#     for i in range(1,10000):
#         a = yield '包子'+str(i)
#         print('a is',a)
#         b = yield '窝窝头'
#         print('b is', b)
# e = eat()
# print(e.__next__())
# print(e.send('大葱'))
# print(e.send('大蒜'))
#
#
# def func():
#     yield 1
#     yield 2
#     yield 3
#     yield 4
#     yield 5
# f = func()
# for i in f:
#     print(i)

import functools


def apple(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        print("start")
        # func(*args,**kwargs)
        print(func.__name__)
        print("end")
        return func(*args, **kwargs)

    return inner


@apple
def chery666():
    # print("chery")
    return "chery888"


chery666()

# from django.db import close_old_connections
# close_old_connections()

# lll = "hfeiwfhdsif"
# ppp =  lll[0:3]
# kkk = [1,2,3,3,3,3,3,3]
# print(f'今年{kkk}')


import types


class AA(object):

    static_data = []

    def __init__(self,static_1):
        self.static_1 = static_1

    def funbbb(self):
        print(self.static_data)

    def func(self,arg):
        # if callable(arg):
        #     print(arg())
        if isinstance(arg,types.FunctionType):
            print(arg())
        else:
            print(arg)

# func("666")
# def funccc():
#     return 2+333333
# func(funccc)


aa = AA('456')
print(AA.static_data)
print(aa.static_1)
AA.static_data.append('777')
AA.static_data.append('888')
print(AA.static_data)
AA('456').funbbb()





