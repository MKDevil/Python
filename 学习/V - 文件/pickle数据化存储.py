#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pickle
# pickle模块是对 python对象 进行 序列化/反序列化 的 二进制协议
# pickle模块有两个过程
# picking：序列化，将 python对象 转换为 字节流
# unpicking：反序列化，将 字节流 转换为 python对象

# pickle使用的数据格式仅用于python
# pickle可以直接表示大部分python数据类型，包括自定义类型

# 序列化和反序列化
# dumps(obj, protocol=None, *, fix_imports=True)
# loads(bytes_object, *, fix_imports=True, encoding='ASCII', errors='strict')

# 文件读写
# dump(obj, file, protocol=None, *, fix_imports=True)
# pickle.(file, protocol).dump(obj)
# load(file, *, fix_imports=True, encoding='ASCII', errors='strict')

# ----------------------------------------    内置数据    ----------------------------------------
dic_a = {'name': '小明', 'age': 14, 'score': 88}

# dumps和loads
my_encode = pickle.dumps(dic_a)
print('pickle.dumps序列化后的结果：\n\t', my_encode)
print('\t序列化后的数据类型：', type(my_encode))

my_decode = pickle.loads(my_encode)
print('pickle.loads反序列化后的结果：\n\t', my_decode)
print('\t反序列化后的数据类型：', type(my_decode))

# dump和load
with open('fileRes\\pickle.pkl', 'wb') as file:
    print('正在写入文件pickle.pkl。。。')
    pickle.dump(dic_a, file)
    print('文件写入完毕！')
with open('fileRes\\pickle.pkl', 'rb') as file:
    print('正在读取文件pickle.pkl。。。')
    bin_content = pickle.load(file)
    print('文件读取完毕！内容为：\n\t', bin_content)


# ----------------------------------------    自定义数据    ----------------------------------------
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


stu1 = Student('小黄', 30, 53)

# dumps和loads
my_encode = pickle.dumps(stu1)
print('pickle.dumps序列化后的结果：\n\t', my_encode)
print('\t序列化后的数据类型：', type(my_encode))

my_decode = pickle.loads(my_encode)
print('pickle.loads反序列化后的结果：\n\t', my_decode)
print('\t反序列化后的数据类型：', type(my_decode))

# dump和load 写入和读取多个对象
with open('fileRes\\pickle.pkl', 'rb+') as file:
    print('正在写入文件pickle.pkl。。。')
    pickle.dump(stu1, file)
    pickle.dump(dic_a, file)
    print('文件写入完毕！')
with open('fileRes\\pickle.pkl', 'rb') as file:
    print('正在读取文件pickle.pkl。。。')
    bin_content = pickle.load(file)
    print(type(bin_content))
    print('文件读取完毕！内容为：\n\t', bin_content.__dict__)
    bin_content = pickle.load(file)
    print(type(bin_content))
    print('文件读取完毕！内容为：\n\t', bin_content)
