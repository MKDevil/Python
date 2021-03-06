#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
作用域法则：
内嵌的模块是全局作用域
全局作用域的作用范围仅限于单个文件
每次调用函数都会创建一个新的本地作用域
函数内的变量，除非声明，否则为本地变量
所有其他的变量名都可以归纳为本地、全局或者内置的


LEGB 法则：
1、“使用”——函数中使用未认证的变量名时，按下列顺序搜索 4 个作用域
本地作用域（L） -> 上一层结构中 def 或 lambda 的本地作用域（E）
-> 全局作用域（G） -> 内置作用域（B）（builtins）
2、“赋值 - 函数中”——在函数中给一个变量名赋值时，会创建或改变本地作用域的变量名
除非它已经在那个函数中声明为全局变量
3、“赋值 - 函数外”——在函数外给一个变量名赋值时，本地作用域 等于 全局作用域

全局变量是最直接的保持状态信息的方法
全局变量在多线程并行运算中，作为共享内存，扮演通信工具的角色
"""

# 示例，全局变量与本地变量----------------------------------------------
x = 99


def fun(y):
    return x + y


print(fun(1))
# 全局变量名：x, fun
# 本地变量名：y

# 示例，global----------------------------------------------------------
x = 99


def fun():
    global x
    x = 101


fun()
print(x)

# 示例，嵌套作用域------------------------------------------------------
x = 99


def fun1():
    x = 102

    def fun2():
        print(x)
    fun2()  # 在 fun2() 运行时，向上查找变量 x 最终查找到 fun1() 的 x = 102


fun1()


# 示例，嵌套作用域------------------------------------------------------
"""
在这个例子中，x = 123 是函数 f2() 的环境变量，与其在 f2() 的先后顺序无关
action = f1() 即运行 f1() 函数，将 f2() 函数返回给 action，将 action 变为 f2() 函数
同时，给 action() 函数设定一个 x = 123 的环境变量
"""


def f1():
    # x = 123

    def f2():
        print('faq', x + 10)
    x = 123
    return f2


action = f1()
action()


# 示例，闭合函数（工厂函数）
"""
m = maker(2) 执行时，将函数名 action 返回给 m，并且将变量 x 的值设置为 2 作为 action 的环境变量
m(3) 执行时，自动赋值 y = 3，同时查找变量 x，向上一级找到执行 m = maker(2) 时记录的 x = 2
"""


def maker(x):
    def action(y):
        return x ** y
    return action


m = maker(2)
print(m(3))


# 示例，闭合函数，使用lambda
def maker(x):
    action = (lambda y: x ** y)  # 在低版本 python 中，会报错
    return action


f = maker(3)
print(f(2))


def maker(x):
    action = (lambda y, x=x: x ** y)  # 这种方法可以在任何版本的 python 中使用
    return action


f = maker(3)
print(f(3))
