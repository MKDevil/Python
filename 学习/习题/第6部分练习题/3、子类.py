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


class MyListSub(MyList):
    classCalls = 0

    def __init__(self, data):
        self.calls = 0
        return super().__init__(data)

    def __add__(self, value):
        MyListSub.classCalls += 1
        self.calls += 1
        return super().__add__(value)

    def stats(self):
        return MyListSub.classCalls, self.calls


if __name__ == '__main__':
    a = MyListSub([1, 2])
    b = MyListSub([3, 4])
    a + b
    a + [3]
    print(a.stats())
    print(b.stats())
