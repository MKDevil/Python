#!/usr/bin/env python
# -*- coding:utf-8 -*-
import math


# 2、参数-----------------------------------------------------------------------
def adder(a, b):
    return a + b


print(adder('111', '222'))
print(adder([1, 2, 3], [3, 4, 5]))
print(adder(2.232, 3.231))


# 3、可变参数-------------------------------------------------------------------
def adder(*args):
    res = args[0]
    for i in args[1:]:
        res += i
    return res


print(adder('111', '222'))
print(adder([1, 2, 3], [3, 4, 5]))
print(adder(2.232, 3.231))
# print(adder(a=1, b=2, c=3, {'c': 3}))  # 无法解析字典


# 4、关键字参数-----------------------------------------------------------------
def adder(good=10, bad=20, ugly=30):
    return good + bad + ugly


print(adder())
print(adder(1, 2, 3))
print(adder(1, 2))
print(adder(ugly=2, good=3))


# 拓展到字典
def adder(**args):
    args = list(args.values())
    res = args[0]
    for i in args[1:]:
        res += i
    return res


print(adder(a=1, b=2, c=3))


# 5、copyDict 函数，复制字典（相当于自己编写的 dict.copy() 函数
def copyDict(old):
    new = {}
    for key in old.keys():
        new[key] = old[key]
    return new


# 6、addDict 函数，求字典的并集
def addDict(dic1, dic2):
    res = {}
    temp = []
    totalKeys = set(dic1.keys()).union(set(dic2.keys()))
    print(totalKeys)
    print(list(dic1.keys()))
    for key in totalKeys:
        if key in list(dic1.keys()):
            temp.append(dic1[key])
        if key in list(dic2.keys()):
            temp.append(dic2[key])
        res[key] = temp.copy()
        print(res)
        temp.clear()
    return res


print(addDict({'a': 1, 'b': 2, 'd': 3}, {'a': 2, 'c': 333, 'd': [1, 2, 3]}))


# 7、判断是否为质数
def prime(num):
    x = num // 2
    while x > 1:
        if num % x == 0:
            print(num, '不是质数！')
            break
        x -= 1
    else:
        print(num, '是一个质数')


# 8、计算系列数字的平方根
li = [2, 4, 9, 16, 25]
# for 循环
res = []
for x in li:
    res.append(pow(x, 0.5))
print(res)
# map 函数
res = []
res = list(map(lambda x: pow(x, 0.5), li))
print(res)
res = []
res = list(map(math.sqrt, li))
print(res)
# 列表解析
res = []
res = [math.sqrt(x) for x in li]
print(res)
