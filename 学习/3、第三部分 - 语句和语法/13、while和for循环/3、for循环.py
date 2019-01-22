#!/usr/bin/env python
# -*- coding:utf-8 -*-

# for 循环是一个通用的序列迭代器，可以遍历任何有序的序列对象内的元素

# for <target> in <object>:
#     <statement1>
# else:
#     <statement2>              没有遇到break语句则会执行

# 每次循环开始时，<target>变量都会被设定为<object>中的下一个元素，无论在循环中对其做了什么样的更改

# 示例，遍历列表
for x in ['spam', 'eggs', 'ham']:
    print(x, end=' ')
print()

# 示例，for循环中的元组赋值
t = [(1, 2), (3, 4), (5, 6)]
for (a, b) in t:
    print(a + b)

# 示例，手动解包
for pack in t:
    a, b = pack
    print(a + b)

# 示例，嵌套解包
t = [((1, 2), 3), ((4, 5), 6), ((7, 8), 9)]
for ((a, b), c) in t:
    print(a, b, c)
t = [((1, 2), 3), ('XY', 6)]
for ((a, b), c) in t:
    print(a, b, c)

# 示例，扩展的序列赋值
t = [(1, 2, 3, 4), (5, 6, 7)]
for (a, *b, c) in t:
    print(a, b, c)

# 示例，字典获取键和值
d = {'a': 1, 'b': 2, 'c': 3}
# 方法一
for key in d:
    print(key, '>>', d[key])
# 方法二
for (key, value) in d.items():
    print(key, '>>', value)

# 示例，获取两个序列中的相同元素
str1 = 'spam'
str2 = 'cam'
# 方法一，嵌套for语句
res = []
for x in str1:
    for y in str2:
        if x == y:
            res.append(x)
            break
    else:
        print(x, 'not found in str2')
print(res)

# 方法二，使用in
res = []
for x in str1:
    if x in str2:
        res.append(x)
    else:
        print(x, 'not found in str2')
print(res)
