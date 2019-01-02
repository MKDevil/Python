#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 任何定义了__enter__()和__exit__()方法的对象，都可以用于上下文管理器
from fileStatus import isOpen

with open('fileRes\\test.txt', 'w') as file:
    isOpen(file)
    content = input('输入你想要的数据：')
    file.write(content)
    print('输入完毕！')
# with...as...结束后，文件自动关闭
isOpen(file)

with open('fileRes\\test.txt', 'r') as file:
    isOpen(file)
    content = file.readlines()
    print(content)
    print('读取完毕！')
isOpen(file)

# 自定义类的上下文管理器


class TestVow(object):
    def __init__(self, text):
        super(TestVow, self).__init__()
        self.text = text

    def __enter__(self):
        self.text = 'I say:' + self.text
        print('打开对象')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.text = self.text + '!'
        print('关闭对象')
        return self


with TestVow('I am fine') as fine:
    pass
