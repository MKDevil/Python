#!/usr/bin/env python
# -*- coding:utf-8 -*-
import shelve
# shelve类似于数据库，内部通过pickle进行序列化
# 只有一个open()方法，用于打开指定的文件，然后返回一个shelf对象
#   其value值可以为任意基本python对象
#   其keys为字符串
# shelve.open(filename, flag='c', protocol=None, writeback=False)
#   flag参数表示打开数据存储文件的格式，取值与dbm.open()一致
#       'r' 以只读方式打开一个已经存在的数据存储文件
#       'w' 以读写方式打开一个已经存在的数据存储文件
#       'c' 以读写模式打开一个数据存储文件，如果不存在则创建
#       'n' 总是创建一个新的、空的数据存储文件，并以读写模式打开
#   protocol 序列化数据所使用的协议版本，默认pickle v3
#   writeback 是否开启回写功能

# 读写完毕后，需要使用 shelve.close() 方法关闭文件
# 建议采用上下文管理器

# ----------------------------------------    内置数据    ----------------------------------------
dic_1 = {'name': '小明', 'age': 14, 'score': 99}
# 写入数据
with shelve.open('fileRes\\shelve\\shelve_dic') as db:
    print('正在写入文件。。。')
    db['小明'] = dic_1
    # for keys,value in dic_1.items():
    # db[keys] = value
    print('文件写入完毕！')

# 读取数据
with shelve.open('fileRes\\shelve\\shelve_dic') as db:
    print('正在读取文件。。。')
    print(db['小明'])
    # for keys, value in dic_1.items():
    # print(keys, ': ', value)
    print('文件读取完毕！')


# ----------------------------------------    内置数据    ----------------------------------------
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def __repr__(self):
        return('学生姓名：%(name)s，年龄：%(age)d，成绩：%(score)d。' % self.__dict__)


stu_tom = Student('Tom', 13, 51)
sut_mike = Student('Mike', 14, 80)
# 写入数据
with shelve.open('fileRes\\shelve\\Student') as db:
    print('正在写入文件。。。')
    db['Tom'] = stu_tom
    db['Mike'] = sut_mike
    print('文件写入完毕！')

# 读取数据
with shelve.open('fileRes\\shelve\\Student') as db:
    print('正在读取文件。。。')
    print(db['Tom'])
    print(db['Mike'])
    print('文件读取完毕！')


# ----------------------------------------    读取和删除    ----------------------------------------
def read_shelve(shelve_name=None):
    with shelve.open('fileRes\\shelve\\Student') as db:
        print('正在读取文件。。。')
        if shelve_name is None:
            for keys in db:
                print(db[keys])
        else:
            print(db[shelve_name])
        print('文件读取完毕！')


def write_shelve(obj, shelve_name=''):
    with shelve.open('fileRes\\shelve\\Student') as db:
        print('正在写入文件。。。')
        shelve_name = obj.__class__.__name__
        db[shelve_name] = obj
        print('文件写入完毕！')


def del_shelve(shelve_name=None):
    if shelve_name == '\n':
        with shelve.open('fileRes\\shelve\\Student') as db:
            del db[shelve_name]
            print('项目删除完毕！')
    else:
        print('未提供参数！')


read_shelve()
del_name = input('输入你想删除的项目:\n\t')
del_shelve(del_name)
read_shelve()
read_shelve('Mike')
mlk = Student('孟令珂', 24, 59.9)
write_shelve(mlk)
read_shelve()
