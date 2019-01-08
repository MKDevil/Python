#!/usr/bin/env python
# -*- coding:utf-8 -*-

# --------------------    列表解析    --------------------
# 建立一个序列
# 使用列表解析
res = [x * 4 for x in 'spam']
print(res)
# 使用for循环
res = []
for x in 'spam':
    res.append(x * 4)
print(res)

# --------------------    索引、分片和矩阵    --------------------
# 索引
print(res[1])
print(res[-1])
# 分片
print(res[1: 3])
print(res[: -1])
print(res[0: len(res)])
# 矩阵
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print('{0[0]}\n{0[1]}\n{0[2]}'.format(matrix))
print(matrix[0][0])
print(matrix[1][2])
print(matrix[2][2])

# --------------------    列表修改    --------------------
# 删除
del res[2:]
print(res)
