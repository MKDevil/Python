#!/usr/bin/env python
# -*- coding:utf-8 -*-

# enumerate(object, start=0) 返回一个生成器对象，可迭代
# 返回值由 (index, value) 组成的一个元组
# index 为偏移
# value 偏移对应的值，如果 object 是字典，value 就是字典的键

# 示例
s = 'spam'
for (index, value) in enumerate(s):
    print('{}>>{}'.format(index, value))

# 示例，使用 next() 函数
e = enumerate(s)
print(next(e))
print(next(e))
print(next(e))
print(next(e))

# 示例，列表解析
print([i * j for(i, j) in enumerate(s)])
