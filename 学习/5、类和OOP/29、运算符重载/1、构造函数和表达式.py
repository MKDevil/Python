#!/usr/bin/env python
# -*- coding:utf-8 -*-
from baseClass import BaseClass


class Department(BaseClass):
    """docstring for Deparment"""

    def __init__(self, departName, departIncome):
        self.departName = departName
        self.departIncome = departIncome

    def __add__(self, other):
        return self.departIncome + other.departIncome

    def __sub__(self, other):
        if self.departIncome > other.departIncome:
            return ('%s 部门比 %s 部门收入高 %s' % (self.departName,
                                            other.departName, self.departIncome - other.departIncome))
        elif self.departIncome == other.departIncome:
            return ('%s 部门与 %s 部门收入相同!' % (self.departName, other.departName))
        else:
            return ('%s 部门比 %s 部门收入高 %s' % (other.departName,
                                            self.departName, other.departIncome - self.departIncome))

    def __mul__(self, other):
        return '警告：该类不支持乘法！'

    def __truediv__(self, other):
        return '警告：该类不支持除法！'


if __name__ == '__main__':
    dev = Department('dev', 65536)
    sell = Department('sell', 66666)
    print(dev + sell)
    print(dev - sell)
    print(dev * 3)
    print(sell / 3)
