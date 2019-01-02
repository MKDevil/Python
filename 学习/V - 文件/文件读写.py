#!usr/bin/env python
# -*- coding:utf-8 -*-


# open(文件名, 打开方式) 创建文件，打开方式有
# r 只读    w 写入
file1 = open('fileRes\\test.txt', 'w')

# write() 写入
file1.write('my name is mlk.\nI like programing.\nI am 24 years old')
file1.close()
# 读取
# 读取N bytes的数据，读取前15个字符
file1 = open('fileRes\\test.txt', 'r')
print(file1.read(15))
file1.close()
# 读取一行
file1 = open('fileRes\\test.txt', 'r')
print(file1.readline())
print(file1.readline())
print(file1.readline())
file1.close()
# 读取所有行，储存在列表中，每个元素是一行
file1 = open('fileRes\\test.txt', 'r')
print(file1.readlines())
file1.close()

# flush 刷新
f = open("fileRes\\test.txt", "w")
f.writelines("tom,11,89\nlili,12,98\nvhjx,25,250")
f.flush()
f.close()
x = open("fileRes\\test.txt", "r")
contents = x.read()
x.close()
print(contents)
