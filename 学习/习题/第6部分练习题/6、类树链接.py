#!/usr/bin/env python
# -*- coding:utf-8 -*-


class ListInstance(object):
    def __str__(self):
        return '<Instance of %s(%s), address %s: \n%s>' % (
            self.__class__.__name__,
            self.__supers(),
            id(self),
            self.__attrnames()
        )

    def __attrnames(self):
        # result = ''
        for attr in sorted(self.__dict__):
            result = '\tname: %s = %s\n' % (attr, self.__dict__[attr])
        return result

    def __supers(self):
        names = []
        for superClass in self.__class__.__bases__:
            names.append(superClass.__name__)
        return ', '.join(names)


if __name__ == "__main__":
    print('-' * 40, '使用 dir 列出实例属性', '-' * 40)

    class Spam(ListInstance):
        def __init__(self):
            self.data1 = 'food'

    # 当继承自 ListInstance 的类，使用打印操作时，自动触发 __str__ 方法
    a = Spam()
    print(a)

    # 还可以将其变为一个字符串，而不用 str 打印出来，并且交互式响应仍然使用默认格式
    str(a)  # 该方式需要在交互式解释器使用

    # 将 ListInstance 类用于混合继承
    class Super(object):
        def __init__(self):
            self.data1 = 'spam'

        def ham(self):
            pass

    class Sub(Super, ListInstance):
        def __init__(self):
            Super.__init__(self)
            self.data2 = 'eggs'
            self.data3 = 42

        def spam(self):
            pass

    b = Sub()
    print(b)
