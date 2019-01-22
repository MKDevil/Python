#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Python 中的文档形式：
形式                  角色
#注释                 文件中的文档
dir函数               对象中可用属性的列表
文档字符串__doc__     附加在对象上的文件中的文档
PyDoc: help函数       对象的交互帮助
PyDoc: HTML报表       浏览器中的模块文档
标准手册              正式的语言和库的说明
网站资源              在线教程、例子等
出版的书籍            商业参考书籍
"""

# 1、文档字符串 __doc__
import doc
print('-' * 40, '\ndoc.py的文档：\n', doc.__doc__)
print('-' * 40, '\ndoc.add的文档：\n', doc.add.__doc__)

# 2、PyDoc: help
print('-' * 40, '\ndoc的帮助文档：\n', help(doc))
print('-' * 40, '\ndoc.add的帮助文档：\n', help(doc.add))

# 3、HTML报表
