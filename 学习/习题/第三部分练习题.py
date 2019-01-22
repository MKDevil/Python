#!/usr/bin/env python
# -*- coding:utf-8 -*-

import random

# 一、基本循环
s = 'spam'
# 1.写一个 for 循环，打印字符串 s 中每个字符的 ASCII 编码
for i in s:
    print(ord(i))

# 2.计算所有 ASCII 码的和
res = 0
for i in s:
    res += ord(i)
print(res)

# 3.返回一个列表，包含 s 中每个字符的 ASCII 码
res = [ord(i) for i in s]
print(res)
# 测试是否与 map(ord, s) 相同
res = map(ord, s)
print(list(res))

# 二、转义字符
for i in range(50):
    print('hello %d\n\a' % i)

# 三、排序字典输出
d = {'c': 3, 'b': 2, 'a': 1, 'f': 20}
for key in sorted(d.keys()):
    print('{}>>{}'.format(key, d[key]))

# 四、查找 2 的幂值的列表
li = [random.randint(0, 1024) for i in range(256)]
pow2 = [2 ** i for i in range(11)]
res = []
for i in pow2:
    if i in li:
        res.append(i)
if res:
    print('找到对应的值：', res)
else:
    print('未找到对应值，运气真差！')
