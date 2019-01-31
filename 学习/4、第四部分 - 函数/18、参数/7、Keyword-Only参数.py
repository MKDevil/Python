#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Keyword-Only 参数：
必须只按照关键字传递并且不会由一个位置参数来填充的参数
出现在 *args 或 * 参数之后
"""


# 示例一
def func(a, *args, c):
    """参数 c 位于 *args 之后，为 Keyword-Only 参数"""
    print(a, args, c)


func(1, 2, 3, 4, 5, c='faq')


# 示例二
def func(a, *, b, c):
    """参数 b, c 位于 * 之后，为 Keyword-Only 参数"""
    print(a, b, c)


func(1, c=2, b=3)
func(b=3, c=2, a=1)
"""
func(b=3, c=2, 1)
    报错：因为 1 作为位置参数，必须出现在关键字参数之后
func(1, 2, 3)
    报错：因为 b, c 均为 Keyword-Only 参数，必须指定
"""


# 示例三
def func(a, *, b='bb', c='cc'):
    print(a, b, c)


func(1)
func(1, c=3, b=2)
func(a=1)
"""
func(1, 2)
    报错：未指定参数
"""


# 示例四，混用 *, Keyword-Only, ** 参数
def func(a, *b, c, d='spam', **e):
    """
    a 是位置参数
    *b 是 *args 参数
    c 是没有默认值的 Keyword-Only 参数
    d 是有默认值的 Keyword-Only 参数
    e 是 **args 参数
    """
    print(a, b, c, d, e)
