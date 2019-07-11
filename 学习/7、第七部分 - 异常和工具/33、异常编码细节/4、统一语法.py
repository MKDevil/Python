#!/usr/bin/env python
# -*- coding:utf-8 -*-


x = [1, 2]

try:
    print(x[1])
except IndexError:
    print('except: 触发 IndexError!')
else:
    print('else: 未触发 IndexError!')
finally:
    print('finally: 程序恢复')
print('异常处理结束！\n\n')

try:
    print(x[2])
except IndexError:
    print('except: 触发 IndexError!')
else:
    print('else: 未触发 IndexError!')
finally:
    print('finally: 程序恢复')
print('异常处理结束！')
