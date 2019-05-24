#!/usr/bin/env python
# -*- coding:utf-8 -*-


def foo(*args, **kwargs):
    print('args=', args)
    print('kwargs=', kwargs)
    print('**********************')


if __name__ == '__main__':
    foo(1, 2, 3)
    foo(a=1, b=2, c=3)
    foo(1, 2, 3, a=1, b=2, c=3)
    foo(1, 'b', 'c', a=1, b='b', c='c')

# ###########################################


def test_var_args(farg, *args):
    print("formal arg:", farg)
    for arg in args:
        print("another arg:", arg)


test_var_args(1, "two", 3)

# ###########################################


def test_var_kwargs(farg, **kwargs):
    print("formal arg:", farg)
    for key in kwargs:
        print("another keyword arg: %s: %s" % (key, kwargs[key]))


test_var_kwargs(farg=1, myarg2="two", myarg3=3)
