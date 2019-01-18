#!/usr/bin/env python
# -*- coding:utf-8 -*-

# zip 用于创建一个元组对的列表，是一个可迭代对象
# 当参数长度不同时，zip 会以最短序列的长度为准

# 示例，zip 迭代两个列表
l1 = [1, 2, 3, 4]
l2 = [5, 6, 7, 8]
for (x, y) in zip(l1, l2):
    print(x, '+', y, '=', x + y)

# 示例，zip 迭代三个元组
t1, t2, t3 = (1, 2, 3), (4, 5, 6), (7, 8, 9)
print(list(zip(t1, t2, t3)))

# 示例，zip 对于不同长度的序列
print(list(zip(l2, t3)))

# 使用zip构造字典
print('\n使用zip构造字典')
dkeys = ['a', 'b', 'c']
dvalues = (1, 2, 3)
# 使用 for 循环为字典添加键值
d1 = {}
for (key, value) in zip(dkeys, dvalues):
    d1[key] = value
print(d1)
# 使用 dict() 方法创建字典
dkeys.reverse()
d2 = dict(zip(dkeys, dvalues))
print(d2)

# map(function, iterable...)
# function 要调用的函数
# iterable 一个或多个序列


# 示例，map的基本用法
print('\nmap的基本用法')


def square(x):
    return x ** 2


print(list(map(square, [1, 2, 3, 4, 5])))

# 示例，使用 lambda 隐性函数
print('\n使用lambda隐性函数')
print(list(map(lambda x, y: x + y, [1, 2, 3], [4, 5, 6, 7])))

# 示例，使用zip与map进行数组的转置
print('\n使用zip与map进行数组的转置')
l3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print('序列l3的内容如下：\n{}\n{}\n{}'.format(*l3))
print('序列l3转置后的内容如下：\n{}\n{}\n{}'.format(*map(list, zip(*l3))))
print('直接用zip转置：\n{}\n{}\n{}'.format(*zip(*l3)))
print('使用map和lambda转置：\n{}\n{}\n{}'.format(
    *map(lambda x, y, z: [x, y, z], *l3)))
