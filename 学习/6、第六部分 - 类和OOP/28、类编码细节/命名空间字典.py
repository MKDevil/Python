#!/usr/bin/env python
# -*- coding:utf-8 -*-


class superClass(object):
    def hello(self):
        self.data1 = 'spam'


class subClass(superClass):
    def hola(self):
        self.data2 = 'eggs'


if __name__ == "__main__":
    X = subClass()
    print(X.__dict__)
    print(X.__class__)
    print(subClass.__bases__)
    print(superClass.__bases__)
    print('1----------------------------------------')

    X.hello()
    print(X.__dict__)
    print('2----------------------------------------')

    X.hola()
    print(X.__dict__)
    print('3----------------------------------------')

    print(subClass.__dict__.keys())
    print(superClass.__dict__.keys())
    print('4----------------------------------------')

    Y = subClass()
    print(Y.__dict__)
    print('5----------------------------------------')

    print(X.data1, X.__dict__['data1'])
    print('6----------------------------------------')

    X.data3 = 'toast'
    print(X.__dict__)
    print('7----------------------------------------')

    X.__dict__['data3'] = 'ham'
    print(X.data3)
