#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 示例1，切掉字符串
s = 'spam'
while s:
    print(s)
    s = s[1:]

# 示例2，循环计算
a = 0
b = 10
while a < b:
    print(a, end=' ')
    a += 1
print('\n')
