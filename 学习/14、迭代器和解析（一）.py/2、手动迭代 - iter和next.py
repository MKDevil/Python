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
