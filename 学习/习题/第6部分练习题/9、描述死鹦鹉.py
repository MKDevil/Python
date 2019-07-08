#!/usr/bin/env python
# -*- coding:utf-8 -*-


class Actor(object):
    def line(self):
        print(self.name, ': ', self.says())


class Customer(Actor):
    name = 'customer'

    def says(self):
        return "that's one ex-bird!"


class Clerk(Actor):
    name = 'clerk'

    def says(self):
        return "no it isn't"


class Parrot(Actor):
    name = 'parrot'

    def says(self):
        return None


class Scene(object):
    def __init__(self):
        self.customer = Customer()
        self.clerk = Clerk()
        self.parrot = Parrot()

    def action(self):
        self.customer.line()
        self.clerk.line()
        self.parrot.line()


if __name__ == '__main__':
    x = Scene()
    x.action()
