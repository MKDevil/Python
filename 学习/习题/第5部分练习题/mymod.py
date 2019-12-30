#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
该文件用于计算文件中的行数和字符数
"""


def countLines(name: 'file'):
    count = 0
    with open(name, 'r', encoding='utf-8') as file:
        for line in file:
            count += 1
    return count


def countChars(name: 'file'):
    count = 0
    with open(name, 'r', encoding='utf-8') as file:
        for line in file:
            count += len(line)
    return count


def test(name):
    return name, countLines(name), countChars(name)


if __name__ == '__main__':
    file = r'E:\渣渣辉\Python\学习\习题\5、第五部分练习题\mymod.py'
    print(countLines(file))
    print(countChars(file))
    print(test(file))
