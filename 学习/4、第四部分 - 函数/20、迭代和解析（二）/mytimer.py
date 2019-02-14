#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time

reps = 1000
repslist = range(reps)


# 计时器 v1.0 ------------------------------------------------------------------
def timer(func, *pargs, **kargs):
    """使用该函数运行指定函数1000次并计时"""
    start = time.process_time()
    for i in repslist:
        ret = func(*pargs, **kargs)
    elapsed = time.process_time() - start
    return (elapsed, ret)


# 计时器 v2.0 ------------------------------------------------------------------
def trace(*args):
    pass


def adv_timer(func, *pargs, **kargs):
    _reps = kargs.pop('_reps', 1000)
    trace(func, pargs, kargs, _reps)
    repslist = range(_reps)
    start = time.process_time()
    for i in repslist:
        ret = func(*pargs, **kargs)
    elapsed = time.process_time() - start
    return (elapsed, ret)


def best_timer(func, *pargs, **kargs):
    _reps = kargs.pop('_reps', 50)
    best = 2 ** 32
    for i in range(_reps):
        (time, ret) = adv_timer(func, *pargs, **kargs)
        if time < best:
            best = time
    return (best, ret)
