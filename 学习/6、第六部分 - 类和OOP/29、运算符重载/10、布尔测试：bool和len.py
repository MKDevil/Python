#!/usr/bin/env python
# -*- coding:utf-8 -*-


class Bool(object):
    def __bool__(self):
        return False


class Len(object):
    def __len__(self):
        return True


X = Bool()
Y = Len()
if not X:
    print('False')
if Y:
    print('True')
