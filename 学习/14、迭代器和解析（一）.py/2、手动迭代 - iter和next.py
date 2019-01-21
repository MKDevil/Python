#!/usr/bin/env python
# -*- coding:utf-8 -*-

# next(object) 自动调用对象的__next__方法


# 示例，计数器，next() 调用 __next__() 方法
class Counter(object):
    def __init__(self, count=0):
        self.count = 0

    def __next__(self):
        self.count += 1
        print('计数：{}'.format(self.count))


counter1 = Counter()
for x in range(10):
    next(counter1)

# iter(object[, sentinel]) 生成迭代器，应用于没有 __next__ 方法的对象
# object 支持迭代的集合对象
# sentinel 如果传递了第二个参数，则参数 object 必须是一个可调用的对象（如 函数）
# 此时，iter 创建了一个迭代器对象，每次调用这个迭代器对象的__next__()方法时，都会调用 object。

# 示例，序列的迭代
li = [1, 2, 3, 4]
li_iter = iter(li)
while True:
    try:
        con = next(li_iter)
    except StopIteration:
        break
    print(con)

# 字典的迭代
# 字典有默认的迭代器，返回的是字典的键
d = {'a': 1, 'b': 2, 'c': 3}
# 方法一
for key in d:
    print(key, '>>', d[key])
# 方法二
for key in d.keys():
    print(key, '>>', d[key])
# 方法三
d_iter = iter(d)
while True:
    try:
        key = next(d_iter)
    except StopIteration:
        break
    print(key, '>>', d[key])
