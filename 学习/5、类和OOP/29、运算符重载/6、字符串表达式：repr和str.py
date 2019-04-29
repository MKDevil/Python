#!/usr/bin/env python
# -*- coding:utf-8 -*-


class Printer(object):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return str(self.value)

    def __str__(self):
        return '实例属于 %s 类，值为 %s' % (self.__class__.__name__, self.value)


A = Printer(88)
print(A)
