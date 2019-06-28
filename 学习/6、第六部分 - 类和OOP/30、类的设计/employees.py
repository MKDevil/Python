#!/usr/bin/env python
# -*- coding:utf-8 -*-


class Employee(object):
    def __init__(self, name, salary=3000):
        self.name = name
        self.salary = salary

    def giveRaise(self, percent):
        self.salary = self.salary * (1 + percent)

    def work(self):
        print(self.name, 'does stuff.')

    def __repr__(self):
        return '<Employee: name=%s, salary=%s>' % (self.name, self.salary)


class Chef(Employee):
    def __init__(self, name):
        super(Chef, self).__init__(name, 5000)  # 厨师的工资定义为5k
        # super().__init__(name, 5000)

    def work(self):
        print(self.name, 'makes food.')


class Server(Employee):
    def __init__(self, name):
        super(Server, self).__init__(name)  # 服务员工资为默认工资3k

    def work(self):
        print(self.name, 'interfaces with customer.')


class PizzaRobot(Chef):
    def __init__(self, name):
        super(PizzaRobot, self).__init__(name)
        # 披萨厨师和普通厨师同等待遇，直接调用普通厨师的构造函数，工资为普通厨师5k

    def work(self):
        print(self.name, 'makes pizza.')


if __name__ == '__main__':
    bob = PizzaRobot('Bob')
    print(bob)
    bob.work()
    bob.giveRaise(0.2)
    print(bob)
    print()
    for klass in Employee, Chef, Server, PizzaRobot:
        obj = klass(klass.__name__)
        obj.work()
