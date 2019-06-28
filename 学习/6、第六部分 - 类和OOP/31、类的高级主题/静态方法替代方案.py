#!/usr/bin/env python
# -*- coding:utf-8 -*-


# 通过类方法对类进行操作--------------------------------------------------
"""缺点
1、只能通过类调用，不能通过实例调用
2、在 Python 2.x 版本无效
"""


class Spam(object):
    numInstances = 0

    def __init__(self):
        Spam.numInstances = Spam.numInstances + 1

    def printNumInstances():
        print('Number of instances created: ', Spam.numInstances)


a = Spam()
b = Spam()
c = Spam()
Spam.printNumInstances()
# b.printNumInstances()  # 这条语句在 Python 2.x 和 Python 3.x 中，都会报错


# 静态方法的替代方案一----------------------------------------------------
"""缺点
1、处理类的函数与类无直接联系，在代码中关系不显著
2、该函数无法继承
"""


def printNumInstances():
    print('Number of instances created: ', Spam.numInstances)


class Spam(object):
    numInstances = 0

    def __init__(self):
        Spam.numInstances = Spam.numInstances + 1


a = Spam()
b = Spam()
c = Spam()
printNumInstances()


# 静态方法的替代方案二----------------------------------------------------
"""缺点
必须要有一个实例才可以调用
"""


class Spam(object):
    numInstances = 0

    def __init__(self):
        Spam.numInstances = Spam.numInstances + 1

    def printNumInstances(self):
        print('Number of instances created: ', Spam.numInstances)


a = Spam()
b = Spam()
c = Spam()
Spam.printNumInstances(b)
# Spam.printNumInstances()  # 不传递实例，会报错
b.printNumInstances()
