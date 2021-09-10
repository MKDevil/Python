'''
Author: MK_Devil
Date: 2021-09-09 16:06:11
LastEditTime: 2021-09-09 16:21:48
LastEditors: MK_Devil
'''
#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 字符串可以用英文单引号、双引号或者三引号标识

# 不转义字符串，在字符串前加 r 字符串内的转义字符将不会转义
a = 'ni\nhao\tsao\ra'
print(a)
a = r'ni\nhao\tsao\ra'
print(a)

# 单引号字符串
a = 'message1'
print(a)

# 双引号字符串
a = "message2"
print(a)

# 单双引号嵌套
a = 'i say:"faq"'
print(a)
a = "i say:'faq'"
print(a)

# 三引号，用于注释
'''这是一个注释'''

# 三引号，保留格式字符串
a = '你好\n我是python'
print(a)
a = '''你好
我是python'''
print(a)
a = '''
你好
我是python
'''
print(a)
