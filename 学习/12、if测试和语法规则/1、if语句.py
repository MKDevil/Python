#!/usr/bin/env python
# -*- coding:utf-8 -*-

# ------------------------------------------------------------------
# --------------------    实现switch类似功能    --------------------
# ------------------------------------------------------------------
# 实例1
choice = 'ham'
print({'spam': 1, 'ham': 1.99, 'eggs': 3, 'bacon': 1.1}[choice])
# 等价于
if choice == 'spam':
    print(1)
elif choice == 'ham':
    print(1.99)
elif choice == 'eggs':
    print(3)
elif choice == 'bacom':
    print(1.1)
else:
    print('Error')

# 实例2，加减乘除的实现1


def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def mul(num1, num2):
    return num1 * num2


def div(num1, num2):
    return num1 / num2


operator = {'+': add, '-': sub, '*': mul, '/': div}
res = operator['+'](1, 2)
print(res)

# 实例3，加减乘除的实现2


def adde():
    return a + b


def sube():
    return a - b


def mule():
    return a * b


def dive():
    return a / b


a = 5
b = 7
operator = {'+': adde(), '-': sube(), '*': mule(), '/': dive()}
res = operator['*']
print(res)

# 更多用法，请看"V - 函数\\switch语句的实现.py"
print("更多用法，请看'V - 函数\\switch语句的实现.py'")

# ------------------------------------------------------------------
# -----------------------    if的通用格式    -----------------------
# ------------------------------------------------------------------
# if 的通用格式
# if <test1>:
#     <statement1>
# elif <test2>:
#     <statement2>
# else:
#     <statement3>


# ------------------------------------------------------------------
# ----------------------    if的三元表达式    ----------------------
# ------------------------------------------------------------------
# A = X if Y else Z
b = 'spams'
a = 'temp' if b == 'spam' else 'test'
print(a)
