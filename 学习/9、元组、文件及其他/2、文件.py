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


with open('test.txt', 'w+') as f:
    f.write('hello!\n')
    f.write('goodbye\n')
    f.flush()
    print(f.readline(), end='')
    print(f.readline(), end='')

# with open('test.txt', 'w') as f:
#     f.write('hello test file!\n')
#     f.write('goodbye test file!\n')

# with open('test.txt', 'r') as f:
#     for line in f:
#         print(line, end = '')  # 不换行，end = '' 取代读取到的 '\n'

# with open('test.txt', 'a') as f:
#     f.write('ass we can!')
