#!/usr/bin/env python
# -*- coding:utf-8 -*-


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


stu1 = Student('小明', 15, 59.9)
print(dir(stu1))
print(stu1.__class__.__name__)
print(stu1.__class__.__dict__)
print(stu1.__dict__)
print(stu1.__class__.__module__)
print(stu1.__module__)
print('\n\n\n\n\n')


def objtodict(obj):
    dic = {}
    dic['__class__'] = obj.__class__.__name__
    dic['__module__'] = obj.__module__
    dic.update(obj.__dict__)
    return dic


objdic = objtodict(stu1)
print(objdic)
class_name = objdic.pop('__class__')
print(class_name)
module_name = objdic.pop('__module__')
print(module_name)
module = __import__(module_name)
print(module)
