#!/usr/bin/env python
# -*- coding:utf-8 -*-

x = set('abcde')
y = set('bdxyz')
print('\'e\' in x：\n\t', 'e' in x)
# 差
print('x - y：\n\t', x - y)
# 与
print('x | y：\n\t', x | y)
# 交
print('x & y：\n\t', x & y)
# 异或
print('x ^ y：\n\t', x ^ y)
# 大于小于
print('x > y：\n\t', x > y)

# 交
z = x.intersection(y)
print('x.intersection(y) == x & y\n\t', z, '==', x & y)

# 添加
z.add('SPAM')
print('z.add(\'SPAM\')：\n\t', z)

z.update(set(['X', 'Y']))
print(z)

z.remove('b')
print(z)

for item in set('abcd'):
    print(item * 3)
