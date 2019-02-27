#!/usr/bin/env python
# -*- coding:utf-8 -*-

from . import pack_1  # 导入当前目录中的 pack_1.py 文件
# from .. import mod_1  # 导入上级目录中的 mod_1.py 文件
# import pack_1  # 使用这种导入方法，单独运行 relative.py 是可以的，但是当 relative.py 作为包导入的时候，就会报错
pack_1.pack_1_pr()
mod_1.mod_1_pr()


def pr():
    print('这是相对导入的一个包！')
