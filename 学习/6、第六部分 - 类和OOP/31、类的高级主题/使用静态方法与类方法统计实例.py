#!/usr/bin/env python
# -*- coding:utf-8 -*-


# 方法一、使用静态方法统计------------------------------------------------
class Spam(object):
    numInstances = 0

    def __init__(self):
        Spam.numInstances += 1

    @staticmethod
    def printNumInstances():
        print('Numbers of instances created: ', Spam.numInstances)


class Sub(Spam):
    @staticmethod
    def printNumInstances():
        print('Extra stuff...')
        # super().printNumInstances()
        # 上述语句会报错，因为超类中的 printNumInstances() 方法为静态方法
        Spam.printNumInstances()


class Other(Spam):
    pass


a = Spam()
b = Spam()
c = Spam()
a.printNumInstances()
Spam.printNumInstances()

d = Sub()
e = Sub()
d.printNumInstances()
Sub.printNumInstances()
Spam.printNumInstances()

f = Other()
f.printNumInstances()
Other.printNumInstances()
Spam.printNumInstances()

print('-' * 30, '测试分割线', '-' * 30)


# 方法二、使用类方法统计--------------------------------------------------
class Spam(object):
    numInstances = 0

    def __init__(self):
        Spam.numInstances += 1

    @classmethod
    def printNumInstances(cls):
        print('Numbers of instances created: ', cls.numInstances)
        # 此处直接使用 cls 调用类


class Sub(Spam):
    @classmethod
    def printNumInstances(cls):
        print('Extra stuff...')
        super().printNumInstances()
        # 此处不会报错，因为超类中的 printNumInstances() 方法为类方法，可以通过 super() 调用


class Other(Spam):
    pass


a = Spam()
b = Spam()
c = Spam()
a.printNumInstances()
Spam.printNumInstances()

d = Sub()
e = Sub()
d.printNumInstances()
Sub.printNumInstances()
Spam.printNumInstances()

f = Other()
f.printNumInstances()
Other.printNumInstances()
Spam.printNumInstances()
