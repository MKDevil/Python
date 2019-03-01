#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
使用以下几种方法，可以获取模块内的指定属性
M.name
M.__dict__['name']
sys.modules['M'].name  # 在 sys.modules 字典中，包含所有的已加载模块
getattr(M, 'name')
"""

seplen = 60
sepchr = '-'
sepline = sepchr * seplen


def listing(module, verbose=True):
    if verbose:
        print(sepline)
        print('name: %s\tfile: %s', module.__name__, module.__file__)
        print(sepline)
    count = 0
    for attr in module.__dict__:
        print('%02d) %s' % (count, attr), end=' ')
        if attr.startswith('__'):
            print('<built-in name>')
        else:
            print(getattr(module, attr))
        count += 1
    if verbose:
        print(sepline)
        print('%s has %d names' % (module.__name__, count))
        print(sepline)


if __name__ == '__main__':
    import formatnum as mod
    listing(mod)
