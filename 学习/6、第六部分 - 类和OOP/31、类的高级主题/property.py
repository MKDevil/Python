#!/usr/bin/env python
# -*- coding:utf-8 -*-


# --------------------    property 的使用    --------------------
class MyClass(object):
    def __init__(self):
        self.__value = 0

    def get_value(self):
        print('get value')
        return self.__value

    def set_value(self, value):
        print('set value')
        self.__value = value

    def del_value(self):
        print('del value')
        del self.__value

    value = property(get_value, set_value, del_value, 'value in MyClass')


x = MyClass()
x.value = 99
print(x.value)

# --------------------  拦截未定义属性的引用  --------------------
# 使用 __getattr__ 方法


class Classic(object):
    def __getattr__(self, name):
        if name == 'age':
            return 40
        else:
            return '未定义的属性' + name


x = Classic()
print(x.age)
print(x.job)


# 使用特性
class Newproperty(object):
    def getage(self):
        return 40
    age = property(getage, None, None, None)


y = Newproperty()
print(y.age)
# print(y.job)  # 会报错，此处不再演示


# --------------------  扩展类，实现属性赋值  --------------------
# 使用 __getattr__ 方法
class Classic(object):
    def __getattr__(self, name):
        if name == 'age':
            return 40
        else:
            return '未定义的属性' + name

    def __setattr__(self, name, value):
        print('set:', name, value)
        # 使用 __dict__ 避免进入死循环
        if name == 'age':
            self.__dict__['age'] = value
        else:
            self.__dict__[name] = value


x = Classic()
print(x.age)

x.age = 41
print(x.age)

x.job = 'dev'
print(x.job)


# 使用特性
class Newproperty(object):
    def getage(self):
        return 40

    def setage(self, value):
        print('set age:', value)
        self.__age = value
    age = property(getage, setage, None, None)


y = Newproperty()
print(y.age)

y.age = 42
print(y.age)

y.job = 'engineer'
print(y.job)
