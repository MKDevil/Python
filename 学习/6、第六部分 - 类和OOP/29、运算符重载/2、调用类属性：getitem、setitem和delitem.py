#!/usr/bin/env python
# -*- coding:utf-8 -*-


class GetItem(object):
    def __init__(self):
        # self.data = [0, 1, 2, 3, 4, 5]
        self.data = 'spam'
        self['A'] = 'AAA'
        self['B'] = 'BBB'

    def __getitem__(self, index):
        """
        __getitem__ 方法
        对于实例进行索引和分片时，会自动调用该方法
        定义该方法后，实例可以作为可迭代对象用于各种迭代环境中
        还可以用于：成员关系测试 in、列表解析、内置函数 map、列表和元组赋值运算、类型构造方法
        """
        print('__getitem__: ', index)
        return self.data[index]

    def __setitem__(self, key, value):
        """
        当类中进行属性赋值 self[key] = value时，会自动调用该方法
        不能在该类中进行属性赋值 self.key = value，否则会进入死循环
        """
        print('__setitem__: %s = %s' % (key, value))
        self.__dict__[key] = value

    def __delitem__(self, key):
        """
        当使用 del instance[key] 删除类属性时，触发该方法
        """
        print('__delitem__: %s' % key)
        del self.__dict__[key]


if __name__ == '__main__':
    x = GetItem()
    print('-' * 30, '索引和分片', '-' * 30)
    print(x[1])
    print(x[-1])
    print(x[0: 3])
    print(x[1: 5: 3])
    print(x[::2])
    print('-' * 30, '迭代环境', '-' * 30)
    for i in x:
        print(i)
    print('-' * 30, '属性赋值', '-' * 30)
    print(x.__dict__)
    x['A'] = 'AAAA'
    x['data'] = 'spamhamegg'
    print(x.__dict__)
    print('-' * 30, '属性删除', '-' * 30)
    print(x.__dict__)
    del x['A']
    print(x.__dict__)
    print('-' * 30, '__getitem__ 的其他用法', '-' * 30)
    print('成员关系测试：', 'p' in x)
    print('列表解析：', [c for c in x])
    print('map函数：', list(map(str.upper, x)))
    print('序列赋值运算：')
    a, *b, c = x
    print(b)
