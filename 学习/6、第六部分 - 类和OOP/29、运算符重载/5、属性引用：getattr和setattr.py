#!/usr/bin/env python
# -*- coding:utf-8 -*-


class Attribute(object):
    def __init__(self, name):
        print('__init__ Start!')
        self.name = name

    def __getattr__(self, key):
        print('__getattr__ Start!')
        try:
            return self.__dict__[key]
        except AttributeError:
            return '没有该属性'

    def __getattribute__(self, key):
        print('__getattribute__ Start!')
        try:
            print('try!')
            # return self.key  # 这种方式会导致死循环
            # return self.__dict__[key]  # 这种方式也会导致死循环
            # return super().__getattribute__(self, key)  # 依旧报错，原因未知
            return object.__getattribute__(self, key)
        except AttributeError:
            print('except!')
            return '__getattribute__: %s not found!' % key

    def __setattr__(self, key, value):
        print('__setattr__ Start!', self.__dict__)
        # self.key = value  # 使用该形式会导致死循环
        self.__dict__[key] = value


X = Attribute('Alice')
print(X.__dict__)
print(X.name)
# print(X['name'])  # 会报错，需要定义 __getitem__ 方法
