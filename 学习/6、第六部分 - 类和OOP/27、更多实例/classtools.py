#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
通用的显示模块
可以显示实例的来源类，实例的各项属性及数值
"""


class attrDisplay(object):
    """
    在创建类的时候，将该类作为超类继承
    可以直接使用 print() 函数打印实例
    """

    def _gatherAttrs(self):
        """
        该函数为类的私有函数，用于获取类的属性和值
        """
        attrs = []
        for key in sorted(self.__dict__):
            attrs.append('%+5s = %-10s' % (key, getattr(self, key)))
        return ', '.join(attrs)

    def __str__(self):
        """
        重写 __str__，当使用 print() 打印类时，自动调用
        """
        return '[%-8s: %s]' % (self.__class__.__name__, self._gatherAttrs())


if __name__ == "__main__":
    class topTest(attrDisplay):
        count = 0

        def __init__(self):
            self.attr1 = topTest.count
            self.attr2 = topTest.count + 1
            topTest.count += 2

    class subTest(topTest):
        pass
    x, y = topTest(), subTest()
    print(x)
    print(y)
