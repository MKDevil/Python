#!/usr/bin/env python
# -*- coding:utf-8 -*-


def kaboom(x, y):
    print(x + y)


try:
    kaboom([0, 1, 2], 'spam')
except TypeError as e:
    print(e.__class__.__name__)
print('resuming here!')
