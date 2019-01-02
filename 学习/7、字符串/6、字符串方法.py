#!/usr/bin/env python
# -*- coding:utf-8 -*-
import base64
s = 'spam'
# --------------------    查询相关    --------------------
print('\n', '-' * 20, '    查询相关    ', '-' * 20)
# count(str) 计算字符串内的某个元素数量
str1 = 'sssssgu'
print('计算字符串str1中\'s\'的数量：\n\t', str1.count('s'))
print('\n')
# endswith(str, [start, [end]]) 字符串是否以字符串str结尾
# startswith(str, [start, [end]]) 字符串是否以字符串str开始
str1 = 'this is a Test stRing!'
print("字符串是否以'ing'结尾：\n\t", str1.endswith('ing'))
print("字符串是否以'ing!'结尾：\n\t", str1.endswith('ing!'))
print("字符串2~5位是否以'is'结尾：\n\t", str1.endswith('is', 2, 5))
print("字符串2~4位是否以'is'结尾：\n\t", str1.endswith('is', 2, 4), str1[2: 4])
print('\n')
print("字符串是否以'th'开始：\n\t", str1.startswith('th'))
print("字符串2~8位是否以'is'开始：\n\t", str1.startswith('is', 2, 8))
print('\n')

# find(str, [start, [end]]) 字符串中指定字符串str的开始位置，查不到则返回-1
# s.rfind(str,[start, [end]]) 字符串中指定字符串str最后出现的位置，查不到返回-1
# index(str, [start, [end]]) 同find，查不到则返回错误，建议使用find！！！！！！！！！！
# s.rindex(str, [start, [end]]) 同rfind
print("字符串中'is'的起始位置为：\n\t", str1.find('is'))
print("字符串中3~8位'is'的位置为：\n\t", str1.find('is', 3, 8))
print('\n')
# replace(old, new, [max]) 用new替换old，最多替换max次
print("将字符串中的'is'替换为'RUOK'：\n\t", str1.replace('is', 'RUOK'))

# --------------------    格式相关    --------------------
print('\n', '-' * 20, '    格式相关    ', '-' * 20)
# --------------------    大小写转换
# upper() 大写
print('str1大写：\n\t', str1.upper())
# lower() 小写
print('str1小写：\n\t', str1.lower())
# capitalize() 第一个字母变成大写，其他字母变小写
print("str1首字母大写：\n\t", str1.capitalize())
# title() 转换为标题格式，所有单词以大写开始
print('将str1转换为标题格式：\n\t', str1.title())
# swapcase() 大小写互换
print("str1大小写互换：\n\t", str1.swapcase())
# casefold() 小写，针对于除英语、汉语以外的其他语言

print('\n')
# --------------------    其他格式相关
# expandtabs(tabsize = 8) 将tab制表符（\t）转换为空格，默认一个tab等于8个空格
str2 = 'this\tis\ta\ttest!'
print('将%s中的制表符转换为空格：\n\t%s' % (str2, str2.expandtabs()))
print('\n')
# ljust(width, [fillchar]) 返回一个原字符串左对齐,并使用空格填充至指定长度的新字符串。默认填充字符为空格。
# center(width, [fillchar]) 返回一个原字符串居中，并使用空格填充至长度 width 的新字符串。
# rjust(width, [fillchar]) 返回一个原字符串右对齐,并使用空格填充至指定长度的新字符串。
# 如果指定的长度小于原字符串的长度则返回原字符串。
s = 'spam'
print('左对齐：\n\t', s.ljust(10, '-'))
print('居中：\n\t', s.center(10, '-'))
print('右对齐：\n\t', s.rjust(10, '-'))

# zfill(width) 返回一个指定长度的字符串，右对齐，填充0
print('右对齐：\n\t', s.zfill(10))
print('\n')

# partition(str) 将字符串按照分隔符str进行分割
# rpartition(str) 从右边开始分割
# 返回一个三元元组，第一个为分隔符之前的，第二个为分隔符本身，第三个为分隔符之后的
print("用'is'分割str1：\n\t", str1.partition('is'))
print('\n')

# split(str, [num]) 分割字符串
# rsplit(str, [num]) 从右边开始分割
# splitlines([keepends]) 按行（\n，\r\n，\r）分割
#   str 分隔符，默认为所有空白字符（空格，\n，\t等）
#   num 分割次数，默认 num = -1 即不限次数
#   keepends 是否保留换行符，默认False
print("str1进行默认模式分割：\n\t", str1.split())
print("str1使用'i'从右边开始分割：\n\t", str1.rsplit('i'))
str2 = 'hello world!\n你好，世界！\nfaq'
print('str2按行分割：\n\t', str2.splitlines())
print('str2按行分割，保留换行符：\n\t', str2.splitlines(True))
print('\n')

# lstrip([char]) 截掉字符串左边的空格或指定字符
# strip([char]) 截掉字符串头尾的空格或指定字符
# rstrip([char]) 截掉字符串右边的空格或指定字符
# 只要头尾有对应其中的某个字符即删除，不考虑顺序，直到遇到第一个不包含在其中的字符为止。
str3 = '88888888123this is a test string!3218888888'
print("截掉左边的'8'：\n\t", str3.lstrip('8'))
print("截掉右边的'8'：\n\t", str3.rstrip('8'))
print("截掉头尾的'128'：\n\t", str3.strip('128'))

# --------------------    is判断类型    --------------------
# isspace() 空格
# isalpha() 字母
# isupper() 大写字母
# islower() 小写字母
# isalnum() 字母+数字
# isdigit 数字
# isnumeric() 数字，只针对Unicode对象
# isdecimal() 十进制字符，只针对Unicode对象
# istitle() 标题格式（单词首字母大写）
# isidentifier() 是否是数字，字母，下划线开头，是否是标准的变量名，是否尊循了变量命名规范
# isprintable() 是否可见（打印输出），有\n等不可见内容，则为False
# isascii() 是否为ASCII码字符（0-127）

# --------------------    修改相关    --------------------
print('\n', '-' * 20, '    修改相关    ', '-' * 20)
# join() 生成一个新的字符串

# --------------------    编码字符串    --------------------
print('\n', '-' * 20, '    编码字符串    ', '-' * 20)
# encode([encoding='utf-8', [errors='strict']]) 编码字符串，第一个参数为要使用的编码，第二个参数为错误处理方案
# decode([encoding='utf-8', [errors='strict']])
# 默认编码模式为 utf-8 ，默认错误处理方案为 strict
# 在python3中，需要将字符串先转换为bytes格式的，然后编码
str1 = 'hello world!孟令珂'
str2 = str1.encode('utf-8')  # 将str2首先编码成为bytes字符串
print('%s编码后的结果为：\n\t%s\n\t类型为：\n\t%s'
      % (str1, str2, type(str2)))
str3 = base64.b64encode(str2)  # 再进行base64编码
print('%s进行base64编码后的结果为：\n\t%s' % (str2, str3))
str4 = base64.b64decode(str3)
print('%s进行base64解码后的结果为：\n\t%s' % (str3, str4))
str5 = str4.decode()
print('%s解码后的结果为：\n\t%s' % (str4, str5))

# --------------------    字符映射（翻译）    --------------------
print('\n', '-' * 20, '    字符映射（翻译）    ', '-' * 20)
str1 = 'this is a Test stRing!wow!!!!!'
# maketrans(intb, outtb) 生成一个映射表，两个参数的长度必须相同
#   intb 想要替换的字符组成的字符串
#   outtb 对应的用于替换的字符组成的字符串
# str.translate(table)
# bytes.translate(table, [delete])
# bytearray.translate(table, [delete])
#   table 翻译表，通过maketrans()方法获得
#   delete 字符串中要过滤的字符列表，不会在结果中出现
str_trans_tb = str.maketrans('aeion', '12345')
print('%s进行映射后的结果为：\n\t%s' % (str1, str1.translate(str_trans_tb)))
str2 = str1.encode()  # 将str1转换为bytes格式的字符串
bytes_trans_tb = bytes.maketrans(b'aeion', b'AEION')  # 建立一个bytes字符串的映射
print("%s进行映射，过滤字符't'和'g'后的结果为：\n\t%s"
      % (str2, str2.translate(bytes_trans_tb, b'tg')))

del str1, str2, str3, str4, str5
