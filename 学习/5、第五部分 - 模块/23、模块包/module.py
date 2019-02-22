#!/usr/bin/env python
# -*- coding:utf-8 -*-

# import modpack.mod_1
# modpack.mod_1.mod_1_pr()
# print(modpack.INIT_X)

# from modpack import *
# mod_1.mod_1_pr()
# mod_2.mod_2_pr()

import modpack.pack.pack_1
"""
这种方法在调用的时候会很麻烦，可以采用以下两种方式调用
import modpack.pack.pack_1 as pack_1
from modpack.pack import pack_1
from modpack.pack.pack_1 import pack_1_pr
第三种方式不建议使用，因为在导入模块中的变量时，有可能会导致覆盖主程序中的同名变量
"""
modpack.pack.pack_1.pack_1_pr()
print(modpack.INIT_X)  # 当载入多重层次的目录时，每级目录的__init__.py都会运行
print(modpack.pack.INIT_X)
