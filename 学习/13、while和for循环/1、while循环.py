#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 实例1，切掉字符串
s = 'spam'
while s:
    print(s)
    s = s[1:]

# 实例2，循环计算
a = 0
b = 10
while a < b:
    print(a, end=' ')
    a += 1
print('\n')

# 实例3，跳出循环
res = a = 0
while True:
    a += 1
    res += a
    if a == 50:
        break
print(res)
