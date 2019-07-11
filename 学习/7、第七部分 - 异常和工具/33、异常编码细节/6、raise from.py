#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
运行下方代码，查看错误输出信息
"""
try:
    1 / 0
except Exception as e:
    raise TypeError('bad!!!!!!!!!!') from e

"""
Traceback (most recent call last):
  File "6、raise from.py", line 8, in <module>
    1 / 0
ZeroDivisionError: division by zero

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "6、raise from.py", line 10, in <module>
    raise TypeError('bad!!!!!!!!!!') from e
TypeError: bad!!!!!!!!!!
"""
