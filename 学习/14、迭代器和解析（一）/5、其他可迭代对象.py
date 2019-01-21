#!/usr/bin/env python
# -*- coding:utf-8 -*-

# range() 返回一个迭代器
# 只支持迭代、索引、len()
# 要获取其列表，需要使用 list() 函数转换
# 没有 __next__() 方法
# 手动进行迭代时，需要使用 iter() 函数生成一个迭代器
print('\n', '-' * 20, '    range()迭代    ', '-' * 20)
r = range(0, 20, 3)
# 对于 range() 的迭代
for i in r:
    print(i, end=' ')
print()
# len()
print('range对象r的长度为：', len(r))
# 对于 range() 的索引
i = 0
while i < len(r):
    print(r[i], end=' ')
    i += 1

# map、zip、filter 迭代器
# 自带 __next__() 方法
# 可以直接使用 next() 进行迭代，无需使用 iter() 函数转换

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


# 用户自定义类的迭代
# 通过 __iter__ 或 __getitem__ 运算符重载使类变得可迭代
# iter() 函数优先调用 __iter__ 方法，如果没有，则调用 __getitem__ 方法
# 示例一，来源：https://www.cnblogs.com/hotbaby/p/4913363.html
class MyIterator():
    def __init__(self, wrapped):
        self.wrapped = wrapped
        self.offset = 0

    def __next__(self):
        if self.offset >= len(self.wrapped):
            raise StopIteration('end')
        item = self.wrapped[self.offset]
        self.offset += 1
        return item


class MyClass():
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        return MyIterator(self.data)


x = MyClass('hello!')
i = iter(x)
while True:
    try:
        print(next(i))
    except Exception as e:
        print(e)
        break


# 示例二，自己写的
class Worker():
    def __init__(self, name, age, pay):
        self.name = name
        self.age = age
        self.pay = pay
        self.offset = 0

    def __next__(self):
        if self.offset == 0:
            self.offset += 1
            return self.name
        elif self.offset == 1:
            self.offset += 1
            return self.age
        elif self.offset == 2:
            self.offset += 1
            return self.pay
        else:
            raise StopIteration

    def __iter__(self):
        return self

    def __getitem__(self, index):
        if index == 0:
            return self.name
        elif index == 1:
            return self.age
        elif index == 2:
            return self.pay
        else:
            raise IndexError

a = Worker('Mike', 22, 4433)
while True:
    try:
        print(next(a))
    except StopIteration:
        break
