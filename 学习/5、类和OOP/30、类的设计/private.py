#!/usr/bin/env python
# -*- coding:utf-8 -*-


class C1(object):
    def meth1(self):
        self.__x = 88

    def meth2(self):
        print(self.__x)


class C2(object):
    def metha(self):
        self.__x = 99

    def methb(self):
        print(self.__x)


class C3(C1, C2):
    pass


a = C3()
a.meth1()
a.metha()
print(a.__dict__)
a.meth2()
a.methb()
