#!/usr/bin/env python
# -*- coding:utf-8 -*-


"""假如编写了如下一段程序，定义了如下异常与代码"""


class Divzero(Exception):
    """除以0的错误"""
    pass


class Overflow(Exception):
    """数值溢出错误"""
    pass


def func():
    """代码库中的方法"""
    pass


"""
捕捉异常方法一
该方法存在如下问题：
当后续更新上述程序，又增加了其他类型的异常后，需要将新增加的异常，也放到 except 语句后的括号中，
这样才能保证捕捉新的异常，严重增加代码量
"""
try:
    func()
except (Divzero, Overflow):
    pass


"""
捕捉异常方法二
该方法存在如下问题：
会捕捉不想要的异常：如内存耗尽、键盘中断（Ctrl + C）、系统退出、try 代码块中的语法错误等
"""
try:
    func()
except:
    pass


"""
捕捉异常方法三
直接在定义异常的时候，使用超类衍生其他异常
只需要列出该超类，就可以捕捉该超类衍生的所有子类异常
"""


class NumError(Exception):
    pass


class Divzero(NumError):
    """除以0的错误"""
    pass


class Overflow(NumError):
    """数值溢出错误"""
    pass


class OtherError(NumError):
    """你想要添加的其他错误类"""
    pass


def func():
    """代码库中的方法"""
    pass


try:
    func()
except NumError:
    pass
