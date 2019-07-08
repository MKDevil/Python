#!/usr/bin/env python
# -*- coding:utf-8 -*-


class MyList(list):
    def __init__(self, data):
        self.data = data[:]

    def __add__(self, value):
        return self.data + value

    def __mul__(self, value):
        return self.data * value

    def __getitem__(self, index):
        return self.data[index]

    def __len__(self):
        return len(self.data)

    def __getslice__(self, start, end):
        return self.data[start: end]

    def append(self, value):
        self.data.append(value)

    def __getattr__(self, name):
        return getattr(self.data, name)

    def __repr__(self):
        return repr(self.data)


a = MyList(['s', 'p', 'a'])
print(a)
print(len(a))
print(a[1: 2])
a.append('m')
a.sort()
print(a)
