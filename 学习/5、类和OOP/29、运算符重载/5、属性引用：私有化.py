#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
更加详细的可以参考第 38 章：修饰器
"""


class PrivateExc(Exception):
    pass


class Privacy(object):
    def __setattr__(self, key, value):
        if key in self.privates:
            raise PrivateExc(key, self)
        else:
            self.__dict__[key] = value


class Test1(Privacy):
    privates = ['age']


class Test2(Privacy):
    privates = ['name', 'pay']

    def __init__(self):
        self.__dict__['name'] = 'Tom'


X = Test1()
Y = Test2()
X.name = 'Bob'
Y.name = 'Sue'
X.age = 30
Y.name = 40
