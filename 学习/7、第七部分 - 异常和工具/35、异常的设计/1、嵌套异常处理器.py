#!/usr/bin/env python
# -*- coding:utf-8 -*-


def action2():
    print(1 + [])


def action1():
    try:
        action2()
    except TypeError:
        print('inner try')


try:
    action1()
except TypeError:
    print('out try')


try:
    try:
        action2()
    except TypeError:
        print('inner try')
except TypeError:
    print('out try')


try:
    try:
        raise IndexError
    finally:
        print('inner finally')
finally:
    print('out finally')
