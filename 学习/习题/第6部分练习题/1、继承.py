#!/usr/bin/env python
# -*- coding:utf-8 -*-


class Adder(object):
    def add(self, x, y):
        print('Not Implemented!')

    def __init__(self, data):
        self.data = data

    def __add__(self, other):
        print('__add__!!!!!!!!!!!!!!!!!!!')
        return self.add(self.data, other)

    def __radd__(self, other):
        print('__radd__!!!!!!!!!!!!!!!!!!!')
        return self.add(other, self.data)


class ListAdder(Adder):
    def add(self, x, y):
        return x + y


class DictAdder(Adder):
    def keys(self):
        return self.data.keys()

    def __getitem__(self, key):
        return self.data[key]

    def add(self, x, y):
        res = {}
        resKeys = sorted(list(set(x.keys()) | set(y.keys())))
        for key in resKeys:
            res[key] = []
            try:
                res[key].append(x[key])
            except KeyError:
                pass
            try:
                res[key].append(y[key])
            except KeyError:
                pass
        return res


a = DictAdder({'a': 1, 'c': 3, 'b': 'ffs'})
b = DictAdder({'f': 343, 'c': 5})
c = {'f': 343, 'c': 5}
print(a + c)
print(a + b)
print(c + a)
