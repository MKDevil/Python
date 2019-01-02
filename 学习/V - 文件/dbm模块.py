#!/usr/bin/env python
# -*- coding:utf-8 -*-
import dbm
import pickle
# dbm模块不能存储自定义对象


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def record(self):
        with dbm.open('fileRes\\dbm\\dbm', 'c') as db:
            dbkey = self.__dict__['name']
            db[dbkey] = pickle.dumps(self)
            print('文件写入完毕！')


def readstu():
    with dbm.open('fileRes\\dbm\\dbm', 'c') as db:
        for key in db.keys():
            content = pickle.loads(db[key])
            print(content)


stu_mike = Student('Mike', 11, 54)
stu_tom = Student('Tom', 12, 66)
stu_alice = Student('alice', 12, 59)
stu_mike.record()
stu_tom.record()
stu_alice.record()
readstu()
