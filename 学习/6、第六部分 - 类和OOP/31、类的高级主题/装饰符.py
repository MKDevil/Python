#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
在类中定义 __get__, __set__, __del__ 方法后
如果没有 __getattribute__ 方法
会自动调用这三个方法进行属性的获取、设置、删除
"""


class Desc(object):
    def __get__(self, instance, owner):
        print('__get__...')
        print('self:\t\t', self)
        print('instance:\t', instance)
        print('owner:\t', owner)

    def __set__(self, instance, value):
        print('__set__...')
        print('self:\t\t', self)
        print('instance:\t', instance)
        print('value:\t', value)


class TestDesc(Desc):
    x = Desc()


t = TestDesc()
t.x
