#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 绑定方法与非绑定方法-----------------------------------------------------------


class Spam(object):
    def doit(self, message):
        print(message)


# 绑定方法
obj1 = Spam()
obj1.doit('faq')

# 非绑定方法
obj2 = Spam()
Spam.doit(obj2, 'ass')


class Eggs(object):
    def m1(self, n):
        print(n)

    def m2(self):
        x = self.m1
        x(42)


Eggs().m2()  # 注意该例子，相比于下面的 Selfless.selfless(3, 4)，该例子使用了 Eggs().m2()，实际上是创建了一个实例对象的


# Python 3，不使用实例调用方法---------------------------------------------------
class Selfless(object):
    def __init__(self, data):
        self.data = data

    def selfless(arg1, arg2):
        print(arg1 + arg2)

    def normal(self, arg1, arg2):
        print(self.data + arg1 + arg2)


a = Selfless(2)
a.normal(3, 4)
Selfless.normal(a, 3, 4)
Selfless.selfless(3, 4)  # 在 Python 2.X 中，该语句会报错，必须要传入一个实例
# Selfless.normal(3, 4)  # 该语句在 Python 2.X 和 Python 3.X 中，都会报错，因为 normal 方法需要一个实例
