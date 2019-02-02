#!/usr/bin/env python
# -*- coding:utf-8 -*-


# 示例一，使用递归函数求和-----------------------------------------------------
def mysum(li):
    if li:
        return li[0] + mysum(li[1:])
    else:
        return 0


print(mysum([1, 2, 3, 4, 5]))


# 使用三元表达式
def mysum(li):
    return li[0] + mysum(li[1:]) if li else 0


print(mysum([1, 2, 3, 4, 5]))


def mysum(li):
    return li[0] if len(li) == 1 else li[0] + mysum(li[1:])


print(mysum([1, 2, 3, 4, 5]))


def mysum(li):
    first, *rest = li
    return first if not rest else first + mysum(rest)


# 示例二，使用递归函数处理任意结构---------------------------------------------
def sumtree(li):
    tot = 0
    for x in li:
        if not isinstance(x, list):
            tot += x
        else:
            tot += sumtree(x)
    return tot


L = [1, [2, [3, 4], 5], 6, [7, 8]]
print(sumtree(L))
