#!/usr/bin/env python
# -*- coding:utf-8 -*-


def isOpen(file):
    if file.closed == True:
        print('文件%s已关闭！' % file.name)
    else:
        print('文件%s已打开！' % file.name)
