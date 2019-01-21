#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 方法一，使用 while循环与 readline() 方法
print('-' * 20, '    方法一： while循环与readline()方法    ', '-' * 20)
with open('test.txt', 'r', encoding='utf-8') as f:
    while True:
        line = f.readline()
        # if line == '':
        if not line:
            # 当line为空字符串时，其bool值为False，not False即为True，语句的意思为：当line为空字符串时，触发 if 事件
            print('文件读取完毕')
            break
        else:
            print(line, end='')
            # 文件中已存在换行符，不用 end='' 的话，输出每行中间会空一行

# 方法二，使用 __next__() 方法
# 如果文件指针已经在最后一行，则会返回 StopIteration 错误
print('-' * 20, '    方法二：__next__()方法    ', '-' * 20)
with open('test.txt', 'r', encoding='utf-8') as f:
    while True:
        try:
            line = f.__next__()
        except StopIteration:
            print('文件已结束，触发错误')
            break
        else:
            print(line, end='')

# 方法三，使用for循环直接迭代文件对象
# 速度最快，语法最简单，强烈推荐！！！！！！！！！！！！！！！！！
print('-' * 20, '    方法三：使用for循环迭代文件对象    ', '-' * 20)
with open('test.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line, end='')
    print('文件读取完毕')

# 方法四，迭代 readlines() 返回的字符串组成的列表
# 此方法会一次性将文件加载到内存，如果文件过大，则容易导致 boom 沙卡拉卡，不建议使用
print('-' * 20, '    方法三：迭代readlines()方法返回的列表    ', '-' * 20)
with open('test.txt', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        print(line, end='')
    print('文件读取完毕')
