#!/usr/bin/env python
# -*- coding:utf-8 -*-


# 示例一，使用递归函数求和-----------------------------------------------------
def mysum(li):
    if li:
        return li[0] + mysum[1:]
    else:
        return 0


print(mysum([1, 2, 3, 4, 5]))
