#!/usr/bin/env python
# -*- coding:utf-8 -*-


class BaseClass(object):
    """docstring for BaseClass"""

    def __init__(self, name, age, pay):
        self.name = name
        self.age = age
        self.pay = pay

    def raisePay(self, raisePercent):
        self.pay *= raisePercent
