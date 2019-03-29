#!/usr/bin/env python
# -*- coding:utf-8 -*-

import manynames

X = 66
print(X)
print(manynames.X)

manynames.f()
manynames.g()

print(manynames.C.X)
I = manynames.C()
print(I.X)
I.m()
print(I.X)
