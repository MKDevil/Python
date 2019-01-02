#!/usr/bin/env python
# -*- coding:utf-8 -*-


def jia(x, y):
    return x + y


def jian(x, y):
    return x - y


def cheng(x, y):
    return x * y


def chu(x, y):
    return x / y


operator = {'+': jia, '-': jian, '*': cheng, '/': chu}
print(operator['+'](3, 2))
