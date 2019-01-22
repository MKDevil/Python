#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 字符串之间可以进行加法合并
s = 'spam'
s += 'SPAM!'
print(s)
s = s[:4] + 'Burger' + s[-1]
print(s)

# replace(str1, str2) 替换字符串
s = 'splot'
s = s.replace('p', 'pam a ')
print(s)
