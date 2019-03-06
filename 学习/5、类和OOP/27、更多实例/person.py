#!/usr/bin/env python
# -*- coding:utf-8 -*-
from classtools import attrDisplay


class Person(attrDisplay):
    """普通员工"""

    def __init__(self, name, job=None, pay=2500):
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):
        """获取姓氏"""
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay = round(self.pay * (1 + percent), 2)

    # def __str__(self):
    #     return '[姓名：%+10s，工作：%+10s，工资：%+10s]' % (self.name, self.job, self.pay)


class Manager(Person):
    """经理"""

    def __init__(self, name, pay=4000):
        # return super().__init__(name, 'mgr', pay)
        Person.__init__(self, name, 'mgr', pay)

    def giveRaise(self, percent, bonus=0.1):
        # self.pay = round(self.pay * (1 + percent + bonus), 2)
        Person.giveRaise(self, percent + bonus)  # 主动调用超类的方法，当超类修改后，也能适应修改


'''
class Manager(object):
    """经理，使用复合对象"""

    def __init__(self, name, pay):
        self.person = Person(name, 'mgr', pay)

    def giveRaise(self, percent, bonus=0.1):
        self.person.giveRaise(percent + bonus)

    def __getattr__(self, attr):
        return getattr(self.person, attr)

    def __str__(self):
        return str(self.person)
'''


class Department(object):
    """部门，使用复合对象"""

    def __init__(self, *args):
        self.members = list(args)

    def addMember(self, person):
        self.members.append(person)

    def giveRaises(self, percent):
        for person in self.members:
            person.giveRaise(percent)

    def showAll(self):
        for person in self.members:
            print(person)


if __name__ == '__main__':
    '''
    # 测试 Person 类
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', 'dev', 3000)
    print(bob)
    print(sue)
    sue.giveRaise(1 / 7)
    print(sue)
    print(sue.lastName())
    # 测试 Manager 类
    tom = Manager('Tom Jones', 5000)
    print(tom.lastName())
    tom.giveRaise(0.1)
    print(tom)
    # 多态
    for object in (bob, sue, tom):
        object.giveRaise(0.1)
        print(object)
    # 复合对象
    development = Department(sue, bob)
    development.addMember(tom)
    development.giveRaises(0.1)
    development.showAll()
    # 内省工具
    print(bob.__class__)
    print(bob.__class__.__name__)
    print(list(bob.__dict__.keys()))
    for key in bob.__dict__:
        print(key, ' => ', bob.__dict__[key])
    for key in bob.__dict__:
        print(key, ' => ', getattr(bob, key))
    '''
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=3000)
    print(bob)
    print(sue)
    print(bob.lastName(), sue.lastName())
    bob.giveRaise(0.1)
    print(bob)
    tom = Manager('Tom Jones', 4500)
    tom.giveRaise(0.1)
    print(tom.lastName())
    print(tom)
