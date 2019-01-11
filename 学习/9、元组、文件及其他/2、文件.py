#!/usr/bin/env python
# -*- coding:utf-8 -*-


# --------------------    打开文件    --------------------
print('-' * 20, '打开文件', '-' * 20)
# open(dir, method)
# dir 为文件路径，如果不想打太多\\可以使用raw字符串
# method 打开方式
# r 只读，没有文件则报错
# w 清空文件，再写入
# a 追加模式（从文件尾部开始写入）
# 加 + 读写模式
# 加 b 二进制模式
# python中的文件对象自带迭代器，以行为单位进行迭代，可以使用for line in file
"""
with open('read.txt', 'r') as f:
    array = f.readlines()
    print(array)
    res = 0
    for x in array:
        a = float(x.rstrip())
        res += a
    print(res)
"""
# --------------------------------------------------------
# --------------------    信息查询    --------------------
# --------------------------------------------------------
f = open('read.txt', 'r+')
print(dir(f))
# fileno() 返回一个整型的文件描述符(file descriptor FD 整型)，可用于底层操作系统的 I/O 操作
print('文件名为：\t', f.name)
print('打开方式为：\t', f.mode)
print('文件描述为：\t', f.fileno())

# isatty() 检测文件是否连接到一个终端设备，是则返回True，否则返回False
if f.isatty:
    print('文件%s已连接到一个终端设备！' % f.name)
else:
    print('文件%s未连接到一个终端设备！' % f.name)

# closed 文件是否关闭
if f.closed:
    print('文件%s已关闭！' % f.name)
else:
    print('文件%s未关闭！' % f.name)

# encoding 获取文件编码
print('%s的编码格式为%s' % (f.name, f.encoding))
print(f.newlines)
f.close()

# --------------------------------------------------------
# --------------------    文件读取    --------------------
# --------------------------------------------------------
f = open('read.txt', 'r+', encoding='utf-8')

# readline() 从当前指针开始，读取一行
print('读取文件的第一行：\n\t', f.readline())

# readlines() 从当前指针开始，读取所有行
print('读取所有行：\n', f.readlines())

# seek(offset[, whence]) 移动文件读取指针到指定位置
# offset 偏移量
# whence 从哪个地方开始计算偏移，默认 0 文件开头，1 当前位置，2 文件末尾
f.seek(0, 0)
print('移动指针到开头第五个字符！')

# read([size]) 从当前指针开始，读取指定的字节数，如果不指定或提供负值，则读取所有
print('从当前指针开始，读取9个字节：\n', f.read(9))

# tell() 返回文件指针的当前位置
print('文件指针的位置为：\n\t', f.tell())

# newlines 当前指针后是否还有行
f.seek(0, 2)
print('当前指针后是否还有行\n\t', f.newlines)

f.close()
# --------------------------------------------------------
# --------------------    文件写入    --------------------
# --------------------------------------------------------
f = open('write.txt', 'w+', encoding='utf-8')

# write(str) 向文件中写入字符串，返回字符串长度
input_str = 'hello world!\n'
input_len = f.write('hello world!\n')
print('写入内容为：\n\t%s\n写入长度为：\n\t%s' % (repr(input_str), input_len))

# writelines(seq) 写入一个序列字符串列表，如需换行，需自行手动添加
input_list = ['my name is \n', 'MK\n', 'age:24']
f.writelines(input_list)
print('写入内容为：\n\t', repr(input_list))

# flush() 刷新文件内部缓冲，将缓冲区数据写入文件
f.flush()
print('刷新内部缓冲！')
f.close()

"""
with open('test.txt', 'w') as f:
    for i in range(0, 3):
        content = input('请输入内容：\n')
        f.write(content)
        if i == 2:
            f.flush()
"""
