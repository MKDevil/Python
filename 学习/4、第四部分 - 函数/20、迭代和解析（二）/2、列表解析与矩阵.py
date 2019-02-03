#!/usr/bin/env python
# -*- coding:utf-8 -*-
MATRIX_INT = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
MATRIX_STR = [['a', 'b', 'c'],
              ['d', 'e', 'f'],
              ['g', 'h', 'i']]

# 示例一、获取矩阵第二列的内容-------------------------------------------------
# 列表解析
res = [row[1] for row in MATRIX_INT]
print(res)
# 等效 for 循环
res = []
for row in MATRIX_INT:
    res.append(row[1])
print(res)


# 示例二、获取矩阵对应位置元素的乘积-------------------------------------------
# 列表解析
res = [MATRIX_INT[row][col] * MATRIX_STR[row][col]
       for row in range(3) for col in range(3)]
print(res)
# 等效 for 循环
res = []
for row in range(3):
    for col in range(3):
        res.append(MATRIX_INT[row][col] * MATRIX_STR[row][col])
print(res)


# 列表解析 - 生成矩阵
res = [[MATRIX_INT[row][col] * MATRIX_STR[row][col]
        for col in range(3)] for row in range(3)]
"""
res = [[MATRIX_INT[row][col] * MATRIX_STR[row][col]
        for row in range(3)] for col in range(3)]
# 这个输出的结果会与上面的有所不同，在于是按照123顺序还是按照147顺序
"""
print(res)

# 等效 for 循环
res = []
for row in range(3):
    temp = []
    for col in range(3):
        temp.append(MATRIX_INT[row][col] * MATRIX_STR[row][col])
    res.append(temp)
print(res)
"""
res = []
for col in range(3):
    temp = []
    for row in range(3):
        temp.append(MATRIX_INT[row][col] * MATRIX_STR[row][col])
    res.append(temp)
print(res)
"""
