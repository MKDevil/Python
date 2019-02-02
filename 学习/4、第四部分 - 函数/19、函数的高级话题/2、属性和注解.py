#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
间接函数调用
可以通过将函数名赋值给一个变量，便可以使用该变量调用函数
也可以通过将函数名嵌套进元组，列表或其他对象中，再进行函数的调用
"""


# 示例一，赋值法间接调用函数---------------------------------------------------
def ptrmsg(message):
    print(message)


x = ptrmsg
x('hello world!')


# 示例二，嵌套元组调用函数-----------------------------------------------------
operator = [(ptrmsg, 'spam'), [ptrmsg, 'faq!']]
for (func, arg) in operator:
    func(arg)


# 示例三，实现 switch 方法-----------------------------------------------------
# 第 17 章（作用域）中，也有类似的示例
def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


operator = {'+': add, '-': sub, '*': mul, '/': div}
res = operator['+'](100, 45)
print(res)
res = operator['-'](100, 45)
print(res)
res = operator['*'](100, 45)
print(res)
res = operator['/'](100, 45)
print(res)


# 函数内省---------------------------------------------------------------------
"""
使用 dir() 函数可以获取函数的各种细节
"""


# 函数属性---------------------------------------------------------------------
"""
可以通过 func.attribute = value 来给函数附加属性
"""


def counter(start=0):
    def counter_in():
        counter_in.count += 1
        return counter_in.count
    counter_in.count = start
    return counter_in


timer = counter(20)
print(timer())
print(timer())
print(timer())


# 函数注解---------------------------------------------------------------------
"""
1、注解只能应用于 def 语句（lambda 不行）
2、对参数的类型、范围以及函数的返回值进行注解
3、注解不会进行类型检查，仅仅是一个注释信息
4、注解存放在 func.__annotations__ 属性中
5、如果有默认参数，则注解要在 = 之前
6、除了在函数装饰器中，注解不会对函数造成任何影响
"""


def func(a: 'spam', b: (1, 10) = 8, c: float = 1.8) -> int:
    return a + b + c


print(func(1, 2, 3))
print(func(1))
print(func.__annotations__)
