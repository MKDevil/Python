#!/usr/bin/env python
# -*- coding:utf-8 -*-


def oops():
    raise IndexError


def other():
    try:
        oops()
    except IndexError:
        print('got IndexError')


if __name__ == '__main__':
    other()

    def oops():
        raise KeyError

    other()
