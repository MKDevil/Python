#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
通用的列表解析的结构：
[ expression for target1 in iterable1 [if condition1]
             for target2 in iterable2 [if condition2] ...
             for targetN in iteralbeN [if conditionN]
]
"""

# 示例一、获取一个字符串中所有字符的 ASCII 编码--------------------------------
st = 'spam'
# 使用 for 循环
res = []
for i in st:
    res.append(ord(i))
print(res)

# 使用列表解析
res = [ord(i) for i in st]
print(res)

# 使用 map
res = list(map(ord, st))
print(res)


# 示例二、求平方---------------------------------------------------------------
# 使用 for 循环
res = []
for i in range(10):
    res.append(i ** 2)
print(res)

# 使用 map
res = list(map(lambda x: x ** 2, range(10)))
print(res)

# 使用列表解析
res = [x ** 2 for x in range(10)]
print(res)


# 示例三、列表解析的测试和嵌套循环---------------------------------------------
# 选出 0~9 之内的偶数
# 使用 for 循环
res = []
for x in range(10):
    if x % 2 == 0:
        res.append(x)
print(res)

# 使用 filter
res = list(filter(lambda x: x % 2 == 0, range(10)))
print(res)

# 使用列表解析
res = [x for x in range(10) if x % 2 == 0]
print(res)


# 示例四、计算 0~9 内所有偶数的平方--------------------------------------------
# 使用 for 循环
res = []
for x in range(10):
    if x % 2 == 0:
        res.append(x ** 2)
print(res)

# 使用 map 和 filter 函数
# 可以看出，lambda 真的是晦涩难懂，妈的一下两下啥都看不出来
res = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, range(10))))
print(res)

# 使用列表解析
res = [x ** 2 for x in range(10) if x % 2 == 0]
print(res)

# 示例五、多重循环的列表解析——组合-------------------------------------------
list1 = ['a', 'b', 'c']
list2 = ['1', '2', '3']
# 使用 for 循环嵌套
res = []
for x in list1:
    for y in list2:
        res.append(x + y)
print(res)

# 使用列表解析嵌套循环
res = [x + y for x in list1 for y in list2]
print(res)

# 示例六、挑选 0~10 中奇数和偶数分别组合---------------------------------------
# 使用 for 循环
res = []
for x in range(10):
    if x % 2 == 0:
        for y in range(10):
            if y % 2 == 1:
                res.append((x, y))
print(res)

# 使用列表解析
res = [(x, y) for x in range(10) if x %
       2 == 0 for y in range(10) if y % 2 == 1]
print(res)
