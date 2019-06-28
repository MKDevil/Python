#!/usr/bin/env python
# -*- coding:utf-8 -*-


class Iters(object):
    def __init__(self, value):
        self.data = value

    def __getitem__(self, i):
        print('get[%s]:' % i, end=' ')
        return self.data[i]

    def __iter__(self):
        """同 __contains__ 一起注释掉，会调用 __getitem__"""
        print('iter:> ', end=' ')
        self.ix = 0
        return self

    def __next__(self):
        print('next:', end=' ')
        if self.ix == len(self.data):
            raise StopIteration
        item = self.data[self.ix]
        self.ix += 1
        return item

    def __contains__(self, x):
        """同 __iter__ 一起注释掉，会调用 __getitem__"""
        print('contains: ', end=' ')
        return x in self.data


a = Iters([1, 2, 3, 4, 5])
print(3 in a)
for i in a:
    print(i, end=' | ')

print()
print([i ** 2 for i in a])
print(list(map(bin, a)))

b = iter(a)
while True:
    try:
        print(next(b), end=' @ ')
    except StopIteration:
        break
