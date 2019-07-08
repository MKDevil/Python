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


a = Set((1, 2, 3))
b = Set([2, 4, 6])
print(a & b)
print(a | b)
c = Set('spam')
print(c[3])
for i in c:
    print(i)
print(c | 'sdf')


class MultiSet(Set):
    def intersect(self, *args):
        res = []
        for i in self:
            for j in args:
                if i not in j:
                    break
                else:
                    res.append(i)
        return Set(res)

    def union(self, *args):
        res = self.data[:]
        for seq in args:
            for i in seq:
                if i not in res:
                    res.append(i)
        return Set(res)


x = MultiSet([1, 2, 3, 4])
y = MultiSet([3, 4, 5])
z = MultiSet([0, 1, 2])
print(x & y)
print(x | y)
print(x.intersect(y, z))
print(x.union(y, z))
print(x.intersect([1, 2, 3], [2, 3, 4], [3, 4, 5]))
print(x.union(range(10)))
