#!/usr/bin/env python
# -*- coding:utf-8 -*-


class Meta(object):
    def __getattr__(self, name):
        print('get: ', name)


x = Meta()
x.append
x.xxx
# x[1]
x[1: 4]
