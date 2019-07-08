#!/usr/bin/env python
# -*- coding:utf-8 -*-


class Lunch(object):
    def __init__(self):
        self.cuntomer = Customer()
        self.employee = Employee()

    def order(self, foodName):
        self.cuntomer.placeOrder(foodName, self.employee)

    def result(self):
        self.cuntomer.printFood()


class Customer(object):
    def __init__(self):
        self.food = None

    def placeOrder(self, foodName, employee):
        self.food = employee.takeOrder(foodName)

    def printFood(self):
        print(self.food.name)


class Employee(object):
    def takeOrder(self, foodName):
        return Food(foodName)


class Food(object):
    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    x = Lunch()
    x.order('pork')
    x.result()
    x.order('pizza')
    x.result()
