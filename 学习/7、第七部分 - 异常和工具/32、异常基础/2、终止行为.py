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
finally:
    print('finally!')
print('contining...')  # 此处定义了 except 用于处理异常，处理结束后，程序继续运行

try:
    fetcher(x, 4)
# except IndexError:
#     print('got exception!')
finally:
    print('finally!')
print('contining...')  # finally 运行后，代码回调至 try，触发异常，终止程序
