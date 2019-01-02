#!/usr/bin/env python
# -*- coding:utf-8 -*-

import string

###################################      字符串常量      ###################################
# ascii_lowercase 生成小写字母 a~z
print('小写字母：', string.ascii_lowercase)

# ascii_uppercase 生成大写字母 A~Z
print('大写字母：', string.ascii_uppercase)

# ascii_letters 生成所有的字母，a~z + A~Z
print('所有字母：', string.ascii_letters)

# digits 数字0~9
print('所有数字：', string.digits)

# hexdigits 十六进制的基础字符 0~9 + A~F
print('十六进制元素：', string.hexdigits)

# octdigits 八进制的基础字符 0~7
print('八进制元素：', string.octdigits)

# punctuation ASCII字符的字符串
print('打印ASCII字符：', string.punctuation)

# whitespace 所有被视为空格的ASCII字符，包括字符空间，制表符，换行符，返回，换行，垂直制表符
print('ASCII中的空格字符：', string.whitespace)

# printable 所有可以被打印的ASCII字符，digits + letters + punctuation + whitespace
print('所有可以被打印的ASCII字符：', string.printable)

###################################      自定义字符串格式      ###################################
# Formatter() string中的一个类，有下列公共方法
# format(format_string, *args, **kwargs)
# vformat(format_string, args, kwargs)
# parse(format_string)
# get_field(field_name, args, kwargs)
# get_value(key, args, kwargs)
# check_unused_args(used_args, args, kwargs)
# format_field(value, format_spec)
# convert_field(value, conversion)

###################################      辅助函数      ###################################
# capwords(str, sep = '') 将每个单词的首字母大写；将每个单词除首字母外小写；将单词之间的多个空格用一个空格代替
# sep的值为你想要的分隔符，默认为空格
strCap = '  ni   haoaaaa sdsaaasdsaaa'
print('测试字符串为：', strCap)
print('string.capwords(strCap) = ', string.capwords(strCap))
print('string.capwords(strCap, sep = “a”) = ',
      string.capwords(strCap, sep='a'))
