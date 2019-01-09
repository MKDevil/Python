#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 元组的方法，元组只有两个方法
# count(x) 查询x在元组中出现的次数
# index(x) 查询x在孕足中第一次出现的位置

# 元组不可变，但是元组中嵌套的内容可以改变
list1 = [2, 3]
print('这里有个一列表：\n\t', list1)
t = (1, list1, 4)
print('将列表作为元组的元素t = (1, list1, 4)\n\t', t)
list1[1] = 99
print('修改列表内的元素list1[1] = 99\n\t', list1)
print('此时元组t的内容为：\n\t', t)
print('-' * 60)
