#!/usr/bin/env python
# -*- coding:utf-8 -*-


class MyError(Exception):
    pass


def oops():
    raise MyError('spam!')


def other():
    try:
        oops()
    except IndexError:
        print('got IndexError')
    except MyError:
        print('got MyError')


if __name__ == '__main__':
    other()
