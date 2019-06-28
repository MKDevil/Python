#!/usr/bin/env python
# -*- coding:utf-8 -*-


# 方法一、使用 staticmethod() 函数----------------------------------------
class ClassType(object):
    def a():
        print('静态方法！')

    def b(cls):
        print('类方法！')

    def c(self):
        print('实例方法！')
    a = staticmethod(a)
    b = classmethod(b)


ClassType.a()
ClassType.b()
# ClassType.c()

x = ClassType()
x.a()
x.b()
x.c()


# 方法二、使用装饰器------------------------------------------------------
class ClassType(object):
    @staticmethod
    def a():
        print('静态方法！')

    @classmethod
    def b(cls):
        print('类方法！')

    def c(self):
        print('实例方法！')


ClassType.a()
ClassType.b()
# ClassType.c()

x = ClassType()
x.a()
x.b()
x.c()
