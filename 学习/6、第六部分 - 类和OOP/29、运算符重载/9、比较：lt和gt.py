#!/usr/bin/env python
# -*- coding:utf-8 -*-


class Test(object):
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        print('__lt__')
        return self.value < other

    def __gt__(self, other):
        print('__gt__')
        return self.value > other

    def __le__(self, other):
        print('__le__')
        return self.value <= other

    def __ge__(self, other):
        print('__ge__')
        return self.value >= other

    def __eq__(self, other):
        print('__eq__')
        return self.value == other

    def __nq__(self, other):
        print('__nq__')
        return self.value != other


X = Test(8)
Y = Test(10)
print(X > 9)
print()
print(9 > Y)
print()
print(X > Y)
