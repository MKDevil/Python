#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 1、包含五个整数0的列表
print('-' * 20, '习题1', '-' * 20)
# 乘法运算
list1 = [0] * 5
print(list1)

# 列表解析
list2 = [0 for i in range(0, 5)]
print(list2)

# append
list3 = []
for i in range(0, 5):
    list3.append(0)
print(list3)

# 2、创建字典，两个键'a', 'b' 值都为0
print('-' * 20, '习题2', '-' * 20)
# 字典解析
dict1 = {x: 0 for x in ('a', 'b')}
print(dict1)

# zip
dict2 = dict(zip(['a', 'b'], [0, 0]))
print(dict2)

# fromkeys()
dict3 = dict.fromkeys(['a', 'b'], 0)
print(dict3)

# 直接使用dict
dict4 = dict(a=0, b=0)
print(dict4)

# 3、列出四种在原处修改列表的方法
print('-' * 20, '习题3', '-' * 20)
# append() 方法
list1.append('faq')
print(list1)

# extend() 方法
list2.extend(list1)
print(list2)

# insert() 方法
list3.insert(1, 99)
print(list3)

# remove() 方法
list3.remove(99)
print(list3)

# pop() 方法
list3.pop()
print(list3)

# del 方法
del list3[1]
print(list3)

# 4、列出四中在原处修改字典的方法
print('-' * 20, '习题4', '-' * 20)
# setdefault() 方法
# update() 方法
# pop() 方法
# popitem() 方法
