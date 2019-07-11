#!/usr/bin/env python
# -*- coding:utf-8 -*-


try:
    raise IndexError('spam')
except IndexError:
    print('got IndexError')
    raise
