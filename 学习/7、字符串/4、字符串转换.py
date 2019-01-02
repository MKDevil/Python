#!/usr/bin/env python
# -*- coding:utf-8 -*-
import string
# --------------------     字符串与数字之间的转换     --------------------
print(repr(42))
print(str(42))
print(float('1.2e5'))
print(repr('spam'))
print(str('spam'))
print("int('1101', 2)：\n\t", int('1101', 2))

# --------------------     字符与ASCII码之间的转换     --------------------
# ord() 将单个字符转换为ASCII码
# chr() 将ASCII码转换为单个字符
print('\n获取所有字母的ASCII码！\n')
# for i in string.ascii_letters:
#     for x in range(0, 3):
#         print('%s\t%d' % (i, ord(i)))
for i in range(0, len(string.ascii_letters), 4):
    print('%s\t%d\t\t\t%s\t%d\t\t\t%s\t%d\t\t\t%s\t%d'
          % (string.ascii_letters[i], ord(string.ascii_letters[i]),
             string.ascii_letters[i + 1], ord(string.ascii_letters[i + 1]),
             string.ascii_letters[i + 2], ord(string.ascii_letters[i + 2]),
             string.ascii_letters[i + 3], ord(string.ascii_letters[i + 3]),
             ))
