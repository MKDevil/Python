#!/usr/bin/env python
# -*- coding:utf-8 -*-


def safe(func, *args):
    func(*args)


if __name__ == '__main__':
    import sys
    try:
        safe(oops, 88)
    except Exception:
        print('got Exception: %s, %s' % (sys.exc_info()[0], sys.exc_info()[1]))
