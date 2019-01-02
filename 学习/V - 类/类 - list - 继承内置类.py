#!usr/bin/env python
# -*- coding:utf-8 -*-


# 定义一个继承于list类的SuperList类，重写list中的减法__sub__
class SuperList(list):
    def __sub__(self, b):
        a = self[:]                 # self[:]   调用self这个列表
        b = b[:]                    # b[:]      调用b这个列表
        while len(b) > 0:
            element_b = b.pop()     # b.pop()   pop方法后未指定参数，即为获取并删除列表b的最后一项
            if element_b in a:
                a.remove(element_b)
        return a                    # 返回减法计算后的a


a = SuperList([1, 2, 3, 4])
b = SuperList([2, 4, 5])
print(a - b)
