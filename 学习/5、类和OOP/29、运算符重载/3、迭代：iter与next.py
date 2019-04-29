#!/usr/bin/env python
# -*- coding:utf-8 -*-


class Squares(object):
    def __init__(self, start, stop):
        self.value = start - 1
        self.stop = stop

    def __iter__(self):
        """声明该对象为可迭代对象"""
        return self  # 返回一个迭代对象，因为目标是让实例本身成为迭代对象，所以返回自身即可

    def __next__(self):
        if self.value == self.stop:
            """当触发结束条件后，抛出一个 StopIteration 异常，迭代会自行结束"""
            raise StopIteration
        self.value += 1
        return self.value ** 2


def fib(end=2000):
    """生成器函数，生成 [0, end) 范围内的斐波那契数列"""
    pre, current = 0, 1
    while current < end:
        yield current
        pre, current = current, current + pre


# 示例：支持重复迭代
class SkipIterator(object):
    def __init__(self, warpped):
        self.warpped = warpped
        self.offset = 0

    def __next__(self):
        if self.offset >= len(self.warpped):
            raise StopIteration
        else:
            item = self.warpped[self.offset]
            self.offset += 2
            return item


class SkipObject(object):
    def __init__(self, warpped):
        self.warpped = warpped

    def __iter__(self):
        return SkipIterator(self.warpped)


if __name__ == '__main__':
    counter = Squares(1, 10)
    for i in counter:
        """
        当for循环运行时，会按照下面两步进行
        1、获得一个可迭代器，即调用 __iter__ 方法
        2、循环的过程，即调用 __next__ 方法
        """
        print(i)
    # __iter__ 只会循环一次，第二次就变味空
    counter = Squares(1, 5)
    a = [i for i in counter]
    b = [j for j in counter]
    print(a)
    print(b)
    # 使用生成器函数，也可以实现类似的操作
    x = fib(200)
    print(list(x))
    x = fib(200)
    for i in x:
        print(i)
    # 支持重复迭代
    alpha = 'abcdef'
    skipper = SkipObject(alpha)
    it = iter(skipper)
    print(next(it), next(it), next(it))
    for i in skipper:
        for j in skipper:
            print(i + j, end=' ')
    print()
    for i in skipper:
        print(i)
