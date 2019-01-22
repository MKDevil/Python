#!/usr/bin/env python
# -*- coding:utf-8 -*-
import struct
import ctypes
# struct 可以将任意数据类型与bytes类型转换


# --------------------    格式化字符串    --------------------
print('-' * 20, '    格式化字符串    ', '-' * 20)
# calcsize(format) 查询一个格式化字符串需要多少字节流存储
format_string = 'f3s2l'
# 该格式化字符串表示可以存储三个数据
# f 一个浮点数（单精度）
# 3s 一个长度为3的字符串
# 2l 两个长整型数字
format_size = struct.calcsize(format_string)
print("格式化字符串内容为'{}'，格式化的数据大小为{}bytes".format(
    format_string, format_size))


# ----------------------------------------------------
# --------------------    打包    --------------------
# ----------------------------------------------------
print('-' * 30, '    打包    ', '-' * 30)

# --------------------    方法一、使用struct.pack()方法    --------------------
# struct.pack(format, v1, v2, ...) 使用format格式进行打包，format与后面的数据数量必须一致
print('-' * 20, '    方法一    ', '-' * 20)
format_string = '9sfi'
print("格式化字符串内容为：\t%s\n格式化字符串长度为：\t%s" %
      (format_string, struct.calcsize(format_string)))
intro_struct_1 = struct.pack(format_string, '孟令珂'.encode(), 24.5, 3000)
print('打包完毕！结果为：\t%s\n打包后的数据长度为：\t%s' % (intro_struct_1, len(intro_struct_1)))

# --------------------    方法二、创建一个带格式化字符串的struct对象    --------------------
# obj.pack(v1, v2, ...)
print('-' * 20, '    方法二    ', '-' * 20)
struct_obj = struct.Struct('9sfi')
print("格式化字符串内容为：\t%s\n格式化字符串长度为：\t%s" %
      (struct_obj.format, struct_obj.size))
intro_struct_2 = struct_obj.pack('孟令珂'.encode(), 24.5, 3000)
print('打包完毕！结果为：\t%s\n打包后的数据长度为\t%s' % (intro_struct_2, len(intro_struct_2)))

# --------------------    方法三、使用struct.pack_into()方法    --------------------
# struct.pack_into(format, buffer, offset, v1, v2, ...)
# offset 偏移，一般情况下0即可
# buffer为可变字符缓冲区，可以避免内存的浪费
# 创建可变字符缓冲区，要与pack后的大小一致
print('-' * 20, '    方法三    ', '-' * 20)
buff_3 = ctypes.create_string_buffer(struct.calcsize(format_string))
values = ('孟令珂'.encode(), 24.5, 3000)
intro_struct_3 = struct.pack_into(format_string, buff_3, 0, *values)
print('打包完毕！结果为：\t%s' % intro_struct_3)
print('数据已经存入可变字符串缓冲区中！')

# --------------------    方法四、使用obj.pack_into()方法    --------------------
# obj.pack_into(buffer, offset, v1, v2, ...)
print('-' * 20, '    方法四    ', '-' * 20)
buff_4 = ctypes.create_string_buffer(struct_obj.size)
intro_struct_4 = struct_obj.pack_into(buff_4, 0, *values)
print('打包完毕！结果为：\t%s' % intro_struct_4)
print('数据已经存入可变字符串缓冲区中！')


# ----------------------------------------------------
# --------------------    解包    --------------------
# ----------------------------------------------------
print('-' * 30, '    解包    ', '-' * 30)

# --------------------    方法一、使用struct.unpack()方法    --------------------
# unpack(format, buffer)
intro_struct_1_unpack = list(struct.unpack(format_string, intro_struct_1))
intro_struct_1_unpack[0] = intro_struct_1_unpack[0].decode()
print("解包完毕，结果为：\t{}".format(tuple(intro_struct_1_unpack)))

# --------------------    方法二、创建一个带格式化字符串的struct对象    --------------------
# obj.unpack(buffer)
intro_struct_2_unpack = list(struct_obj.unpack(intro_struct_2))
intro_struct_2_unpack[0] = intro_struct_2_unpack[0].decode()
print("解包完毕，结果为：\t{}".format(tuple(intro_struct_2_unpack)))

# --------------------    方法三、使用struct.unpack_from()方法    --------------------
# struct.unpack_from(format, buffer, offset) 偏移默认为0
intro_struct_3_unpack = list(struct.unpack_from(format_string, buff_3))
intro_struct_3_unpack[0] = intro_struct_3_unpack[0].decode()
print("解包完毕，结果为：\t{}".format(tuple(intro_struct_3_unpack)))

# --------------------    方法四、使用obj.unpack_from()方法    --------------------
# obj.unpack_from(buffer, offset) 偏移默认为0
intro_struct_4_unpack = list(struct_obj.unpack_from(buff_4))
intro_struct_4_unpack[0] = intro_struct_4_unpack[0].decode()
print("解包完毕，结果为：\t{}".format(tuple(intro_struct_4_unpack)))
