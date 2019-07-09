#!/usr/bin/env python
# -*- coding:utf-8 -*-


def fetcher(obj, index):
    """该函数用于索引"""
    return obj[index]


x = [1, 2]
try:
    fetcher(x, 4)
except IndexError:
    print('got exception!')
print('contining...')
