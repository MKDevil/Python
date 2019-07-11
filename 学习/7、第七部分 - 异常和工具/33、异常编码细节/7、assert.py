#!/usr/bin/env python
# -*- coding:utf-8 -*-


def f(x):
    assert x < 0, 'x must be negative'
    return x ** 2


if __name__ == '__main__':
    try:
        f(1)
    except Exception as e:
        print(e.__class__.__name__)
        print(e)

    print(f(-2))

    f(3)
"""输出结果
AssertionError
x must be negative
4
Traceback (most recent call last):
  File "7、assert.py", line 19, in <module>
    f(3)
  File "7、assert.py", line 6, in f
    assert x < 0, 'x must be negative'
AssertionError: x must be negative
"""
