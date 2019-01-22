#!/usr/bin/env python
# -*- coding:utf-8 -*-

print(range(5))  # 单参数，[0, 5)
print(range(-3, 4))  # 双参数， [a, b)
print(range(1, 10, 2))  # 三参数，[a, b) 步进 c

# 示例，简单的遍历序列
str1 = 'spam'
# 直接遍历序列
for x in str1:
    print(x, end=' ')
print()
# 通过 range(len(X)) 遍历
for x in range(len(str1)):
    print(str1[x], end=' ')
print()

# 示例，非完备遍历
str1 = 'abcdefghijklmn'
# 通过分片
for x in str1[::2]:
    print(x, end=' ')
print()
# 通过 range
for x in range(0, len(str1), 2):
    print(str1[x], end=' ')
print()

# 示例，修改序列
list1 = [1, 2, 3, 4, 5]
# range 遍历并赋值
for x in range(len(list1)):
    list1[x] += 1
print(list1)
# while 方法
i = 0
while i < len(list1):
    list1[i] += 1
    i += 1
print(list1)
# 列表解析
list1 = [x + 1 for x in list1]
print(list1)
