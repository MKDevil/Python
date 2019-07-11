#!/usr/bin/env python
# -*- coding:utf-8 -*-


class MyError(Exception):
    pass


def stuff(file):
    raise MyError


file = open('data', 'w')
try:
    stuff(file)
finally:
    file.close()
    print('not reached')
"""
无论是否触发异常，file 文件总是会关闭
这样可以保证文件输出缓存区的内容已经保存到磁盘
同理，通过这个结构，还可以实现
1、保证服务器连接在出错时关闭
2、保证数据库连接在出错时关闭
3、其他类似的情况
"""
