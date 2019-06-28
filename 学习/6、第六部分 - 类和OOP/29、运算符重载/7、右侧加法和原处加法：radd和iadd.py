#!/usr/bin/env python
# -*- coding:utf-8 -*-


class Adder(object):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return '<Adder: %s>' % self.value

    def __add__(self, other):
        print('__add__:\t %s + %s' % (self, other))
        return self.value + other

    def __radd__(self, other):
        print('__radd__:\t %s + %s' % (self, other))
        return other + self.value

    def __iadd__(self, other):
        print('__iadd__:\t %s + %s' % (self, other))
        self.value += other
        return self


x = Adder(88)
y = Adder(99)
print(x + 5)
print(6 + y)
print(x + y)
x += 888
