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

# 示例3，while...else...循环
y = str(input('输入你想测试的数字'))
x = y // 2
while x > 1:
    if y % x == 0:
        # print(y, 'has a factor:', x)
        break
    x -= 1
else:
    """当while循环正常结束时（非return、break等语句特殊结束），触发else语句"""
    print(y, '是一个质数')
