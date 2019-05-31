#!/usr/bin/env python
# -*- coding:utf-8 -*-


def factory(aClass, *args):
    return aClass(*args)


class Spam(object):
    def doit(self, message):
        print(message)


class Person(object):
    def __init__(self, name, job):
        self.name = name
        self.job = job


object1 = factory(Spam)
object2 = factory(Person, 'Alice', 'engineer')
