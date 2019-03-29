#!/usr/bin/env python
# -*- coding:utf-8 -*-
from abc import ABCMeta, abstractmethod


class SuperClass(metaclass=ABCMeta):
    @abstractmethod
    def method(self):
        print('This is an abstract class')


class MyClass(SuperClass):
    def myMethod(self):
        print('myMethod')


a = MyClass()
a.method()
b = SuperClass()
