#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 示例一，普通参数-------------------------------------------------------------
print('-' * 30, '    普通参数    ', '-' * 30)


def func(a, b, c):
    print(a, b, c)


func(1, 2, 3)

# 示例二，关键字参数，使用关键字传入参数
func(a=2, b=1, c=3)
func(3, c=2, b=1,)
# 如果使用 func(3, a=2, b=1) 则会报错，需要注意，
# 因为默认先分配非关键字参数，再分配关键字参数，a 相当于赋值了两次


# 示例二，默认参数-------------------------------------------------------------
print('-' * 30, '    默认参数    ', '-' * 30)
def func(a, b=2, c=3):
    print(a, b, c)


func(1)
func(a=1)
func(1, 7)
func(1, 3, 5)
