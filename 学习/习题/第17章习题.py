#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
1、下面的代码会输出什么？
x = 'spam'
def func():
    print(x)
func()

输出：spam
按照LEGB法则，想上层作用域查找


2、下面的代码会输出什么？
x = 'spam'
def func():
    x = 'NI'
func()
print(x)

输出：
spam
func()函数中的 x 为函数的本地变量，仅在函数内有效


3、下面的代码会输出什么？
x = 'spam'
def func():
    x = 'NI'
    print(x)
func()
print(x)

输出：
NI
spam
func()函数中的 x 为函数本地变量，仅在函数内有效

4、下面的代码会输出什么？
x = 'spam'
def func():
    global x
    x = 'NI'
func()
print(x)

输出：
NI
使用global，声明 x 为全局变量，之后将 x 赋值为 'NI'
运行func()函数，此时全局变量 x 的值就变成了 'NI'
之后打印变量 x，值为 'NI'


5、下面的代码会输出什么？
x = 'spam'
def func():
    x = 'NI'
    def nested():
        print(x)
    nested()
func()
print(x)

输出：
NI
spam
运行func()函数，从内部调用nested()函数，x = 'NI' 作为函数 nested() 的状态传递给 nested()，因此输出 NI
同时，func() 中的 x 为本地变量，不会影响全局作用域的 x 的值


6、下面的代码会输出什么？
def func():
    x = 'NI'
    def nested():
        nonlocal x
        x = 'spam'
    nested()
    print(x)
func()

输出：
spam
函数 nested() 中，声明 x 不是本地变量，自动向上一层找到 func() 函数中定义的 x = 'NI'
然后 nested() 运行，将 x 赋值为'spam'，函数 func() 中的变量也对应的改变
"""
