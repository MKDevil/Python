#!/usr/bin/env python
# -*- coding:utf-8 -*-


class Set(object):
    def __init__(self, value=[]):
        self.data = []
        self.concat(value)

    def intersect(self, other):
        res = []
        for x in self.data:
            for y in other:
                res.append(y)
        return Set(res)

    def union(self, other):
        res = self.data[:]
        for x in other:
            if x not in res:
                res.append(x)
        return Set(res)

    def concat(self, value):
        for x in value:
            if x not in self.data:
                self.data.append(x)

    def __len__(self): return len(self.data)
    def __getitem__(self, key): return self.data[key]
    def __and__(self, other): return self.intersect(other)
    def __or__(self, other): return self.union(other)
    def __repr__(self): return 'Set:' + repr(self.data)


if __name__ == '__main__':
    x = Set([1, 3, 5, 7])
    print(x.union(Set([1, 4, 7])))
    print(x | Set([1, 4, 6]))
