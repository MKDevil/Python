#!/usr/bin/env python
# -*- coding:utf-8 -*-

# print() 函数的基本形式
# print([object, ...][, sep = ' '][, end = '\n'][, file = sys.stdout])
# sep, end, file 如果给出，必须作为关键字参数给定，即 name = value
# sep 在每个对象的文本之间插入的一个字符串，默认为单个空格；传递一个空字符串将会抑制分隔符
# end 文本末尾的字符串，默认 \n 换行符
# file 指定了文本要发送到的文件、标准流或其他类似文件的对象
# 带有一个类似文件的 write(string) 方法的任何对象对可以传递，前提是文件已经以写入模式打开

# 实例
str1 = 'hello'
str2 = 'world'
with open('test.txt', 'w', encoding='utf-8') as f:
    print(str1, str2, sep='分隔符', end='结束符', file=f)

# 重定向流
# import sys
# sys.stdout = 'test.txt'
# 可以将所有的 print 函数的输出都重定向到 'test.txt'
with open('test.txt', 'a', encoding='utf-8') as f:
    print('hello', file=f)
