#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
常规函数：返回一个值后，退出函数
生成器函数：返回一个值后，从其退出的地方继续的函数

创建生成器：两种方法
变量名 = (列表解析表达式)
yield 表达式

TODO:生成器函数的学习
廖雪峰的网站：
https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014317799226173f45ce40636141b6abc8424e12b5fb27000
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
