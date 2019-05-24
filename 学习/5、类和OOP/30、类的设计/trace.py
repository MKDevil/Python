#!/usr/bin/env python
# -*- coding:utf-8 -*-


class Wrapper(object):
    def __init__(self, object):
        self.wrapped = object

    def __getattr__(self, attrname):
        print('Trace: ', attrname)
        return getattr(self.wrapped, attrname)


if __name__ == '__main__':
    x = Wrapper([1, 2, 3])
    x.append(4)
    print(x)  # 在 Python 3 中，打印不会触发 __getattr__，因此打印输出结果不会是普通打印的结果
