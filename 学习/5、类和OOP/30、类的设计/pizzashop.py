#!/usr/bin/env python
# -*- coding:utf-8 -*-
from employees import PizzaRobot
from employees import Server


class Customer(object):
    def __init__(self, name):
        self.name = name

    def order(self, server):
        print(self.name, ' orders from ', server)

    def pay(self, server):
        print(self.name, ' pays for item to ', server)


class Oven(object):
    def bake(self):
        print('oven bakes')


class PizzaShop(object):
    def __init__(self):
        self.server = Server('Pat')
        self.chef = PizzaRobot('Bob')
        self.oven = Oven()

    def order(self, name):
        customer = Customer(name)
        customer.order = (self.server)
        self.chef.work()
        self.oven.bake()
        customer.pay(self.server)


if __name__ == '__main__':
    scene = PizzaShop()
    scene.order('Homer')
    print('...')
    scene.order('Shaggy')
