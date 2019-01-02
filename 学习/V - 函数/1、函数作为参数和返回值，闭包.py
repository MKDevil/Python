#!/usr/bin/env python
# -*- coding:utf-8 -*-


# --------------------    函数作为参数    --------------------
def square_sum(a, b):
    return a**2 + b**2


def cubic_sum(a, b):
    return a**3 + b**3


def arg_demo(fun, a, b):
    return fun(a, b)


print(arg_demo(square_sum, 3, 5))
print(arg_demo(cubic_sum, 3, 5))


# --------------------    函数作为参数    --------------------
def line_conf():
    def line(x):
        return 2 * x + 1
    return line


my_line = line_conf()  # my_line被赋值为line()函数，my_line类型为函数，函数名为line()
print(my_line(5))
print(my_line.__name__)


# --------------------    闭包与环境变量    --------------------
def line_conf():
    b = 15  # b在line()中引用了，称为line()的环境变量

    def line(x):
        return 2 * x + b
    b = 5
    return line
# 闭包中包含的对象，是内部函数返回时外部对象的值，b = 5 被引用，b = 15 则无效
# 环境变量的位置不影响内部函数的执行，前后均可


my_line = line_conf()
print(my_line(5))
