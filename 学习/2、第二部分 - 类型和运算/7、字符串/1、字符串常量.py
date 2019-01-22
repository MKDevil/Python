#!/usr/bin/env python
# -*- coding:utf-8 -*-

print('---------------字符串常量的各种形式！---------------\n')
s = 'spa''m'
print('单引号\'spa\'\'m\'：\n\t', s)
print('相连的两个字符串会自动合并！\n')

s = "spa'm"
print('双引号"spa\'m"：\n\t', s)
print('单双引号复用，可以在单引号内加双引号，或者双引号内加单引号！\n')

s = '''spam'''
print("三引号'''spam'''：\n\t", s)
print('三引号可以直接打出多行内容：')
s = """Fuck
 you,
  man!\n"""
print(s)

s = 'spa\n\tm'
print(r"转义字符：'spa\n\tm'", '\n\t', s, '\n')

s = r'sp\na\tm'
print(r"Raw字符串（不转义）r'sp\na\tm'：", '\n\t', s, '\n')

s = b'sp\x01am'
print('Byte字符串：\n\t', s, '\n')

s = u'eggs\u0020spam'
print(r"Unicode字符串u'eggs\u0020spam'：", '\n\t', s, '\n')
