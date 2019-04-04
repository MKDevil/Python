#!/usr/bin/env python
# -*- coding:utf-8 -*-
import baseClass


class Deparment(baseClass):
    """docstring for Deparment"""
    def __init__(self, departName, departIncome):
        self.departName = departName
        self.departIncome = departIncome

    def __add__(self, other):
        return self.departIncome + other.departIncome
