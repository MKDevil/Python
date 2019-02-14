#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
常规函数：返回一个值后，退出函数
生成器函数：返回一个值后，从其退出的地方继续的函数

应用：
设定某种规则用于生成无限数量的数字，根据使用情况使用其前 n 项
减少麻烦

生成器表达式：
    变量名 = (列表解析表达式)
生成器函数：
    yield 表达式
"""
# 示例一，创建和读取生成器-------------------------------------------------------
# 使用圆括号创建
gen = (x ** 2 for x in range(7))
print(next(gen))
print(gen.__next__())
print(gen.send(77))
print(gen.send(None))
print(gen.__next__())

for i in gen:
    print('for', i)


# 示例二，列出斐波那契数列的前 n 项-----------------------------------------------
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1
    print('done')


f = fib(5)
for i in f:
    print(i)


# 使用 for 循环编写
def fibfor(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n += 1
    print('done')


fibfor(5)

# 示例三，杨辉三角---------------------------------------------------------------
"""
杨辉三角的形式
        1
      1   1
    1   2   1
  1   3   3   1
"""


def triangles():
    li = [1]
    while True:
        yield li
        lx = [1]
        for i in range(len(li)-1):
            """
            这个 for 循环用于添加杨辉三角中间部分的数据
            中间数据的数量等于这一行的长度减去2，最小为0
            因为 range 函数是左开右闭的区间，使用 len(li) - 1 即可
            当 li 只有一项的时候，len(li) - 1 的值为0
            range(0) 的结果序列是空 []，空列表无法进行迭代
            当第一次运行到 for 循环时，会自动跳过此次循环
            """
            lx.append(li[i] + li[i + 1])
        lx.append(1)
        li = lx.copy()
        lx.clear()


n = 0
for i in triangles():
    print(i)
    n += 1
    if n == 10:
        break

# 使用列表解析简化代码-----------------------------------------------------------


def triangles():
    li = [1]
    while True:
        yield li
        li = [1] + [li[i] + li[i + 1] for i in range(len(li) - 1)] + [1]


n = 0
for i in triangles():
    print(i)
    n += 1
    if n == 10:
        break


# 示例四，斐波那契数列无限写出----------------------------------------------------
def fib():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b


f = fib()
for i in range(20):
    print(f.__next__())
