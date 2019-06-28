#!/usr/bin/env python
# -*- coding:utf-8 -*-


class Student(object):
    __slots__ = ('name', 'age')


tom = Student()
tom.name = 'tom'
tom.age = 15
# tom.score = 80  # 报错，__slots__ 限制实例修改属性

Student.score = 60
print(tom.score)  # 正常打印，证明 __slots__ 对类本身没有约束作用
# tom.score = 88  # 报错，__slots__ 限制实例修改属性
print(tom.score)
