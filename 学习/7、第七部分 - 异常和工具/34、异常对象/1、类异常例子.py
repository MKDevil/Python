#!/usr/bin/env python
# -*- coding:utf-8 -*-


class General(Exception):
    pass


class Specific1(General):
    pass


class Specific2(General):
    pass


def raiser0():
    raise General()


def raiser1():
    raise Specific1()


def raiser2():
    raise Specific2()


for func in (raiser0, raiser1, raiser2):
    try:
        func()
    except General:
        import sys
        print('caught: ', sys.exc_info()[0])


for func in (raiser0, raiser1, raiser2):
    try:
        func()
    except General as err:
        print('caught: ', err.__class__)
