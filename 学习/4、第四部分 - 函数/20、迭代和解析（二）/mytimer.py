#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time
reps = 1000
resplist = range(reps)


def timer(func, *pargs, **kargs):
    """使用该函数运行指定函数1000次并计时"""
    start = time.process_time()
    for i in resplist:
        ret = func(*pargs, **kargs)
    elapsed = time.process_time() - start
    return (elapsed, ret)
