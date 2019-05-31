#!/usr/bin/env python
# -*- coding:utf-8 -*-


class ListInstance(object):
    """
    使用 __dict__ 列出实例属性
    """

    def __str__(self):
        return '<Instance of %s, address %s:\n%s>' % (
            self.__class__.__name__, id(self), self.__attrnames())

    def __attrnames(self):
        # result = ''
        for attr in sorted(self.__dict__):
            result = '\tname: %s = %s\n' % (attr, self.__dict__[attr])
        return result


class ListInherited(object):
    """
    使用 dir 列出继承的属性
    """

    def __str__(self):
        return '<Instance of %s, address %s:\n%s>' % (
            self.__class__.__name__, id(self), self.__attrnames())

    def __attrnames(self):
        result = ''

        for attr in dir(self):
            if attr[:2] == '__' and attr[-2:] == '__':
                result += '\tname: %s = <>\n' % attr
            else:
                result += '\tname: %s = %s\n' % (attr, getattr(self, attr))
        return result


class ListTree(object):
    """列出类树中每个对象的属性"""

    def __str__(self):
        self.__visted = {}
        return '<Instance of {0}, address {1}:\n{2}{3}>'.format(
            self.__class__.__name__,
            id(self),
            self.__attrnames(self, 0),
            self.__listclass(self.__class__, 4))

    def __listclass(self, aClass, indent):
        dots = '.' * indent
        if aClass in self.__visted:
            return '\n{0}<Class {1}:, address {2}: (see above)>\n'.format(
                dots, aClass.__name__, id(aClass))
        else:
            self.__visted[aClass] = True
            genabove = (self.__listclass(c, indent + 4)
                        for c in aClass.__bases__)
            return '\n{0}<Class {1}, address {2}:\n{3}{4}{5}>\n'.format(
                dots,
                aClass.__name__,
                id(aClass),
                self.__attrnames(aClass, indent),
                ''.join(genabove),
                dots)

    def __attrnames(self, obj, indent):
        spaces = ' ' * (indent + 4)
        result = ''
        for attr in sorted(obj.__dict__):
            if attr.startswith('__') and attr.endswith('__'):
                result += spaces + '{0} = <>\n'.format(attr)
            else:
                result += spaces + \
                    '{0} = {1}\n'.format(attr, getattr(obj, attr))
        return result


if __name__ == "__main__":
    # 使用 __dict__ 列出实例属性-----------------------------------------------
    print('-' * 40, '使用 __dict__ 列出实例属性', '-' * 40)

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

    # 使用 dir 列出继承的属性--------------------------------------------------
    print('-' * 40, '使用 dir 列出继承的属性', '-' * 40)

    class Sub2(Super, ListInherited):
        def __init__(self):
            Super.__init__(self)
            self.data2 = 'eggs'
            self.data3 = 42

        def spam(self):
            pass

    c = Sub2()
    print(c)

    # 列出类树中每个对象的属性-------------------------------------------------
    print('-' * 40, '列出类树中每个对象的属性', '-' * 40)

    class Sub3(Super, ListTree):
        def __init__(self):
            Super.__init__(self)
            self.data2 = 'eggs'
            self.data3 = 42

        def spam(self):
            pass
    d = Sub3()
    print(d)
