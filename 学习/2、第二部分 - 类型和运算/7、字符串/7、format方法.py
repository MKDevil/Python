#!/usr/bin/env python
# -*- coding:utf-8 -*-

print('\n', '-' * 20, '    格式化字符串    ', '-' * 20)
# 1、不指定位置，按默认顺序
print('{} {}!'.format('hello', 'world'))
# 2、指定位置，按位置使用，可以重复使用
print('我叫{1}{0}，姓{1}，名{0}。'.format('令珂', '孟'))
# 3、指定名称参数
print('网站名：{name}，地址：{url}'.format(name='runnoob', url='www.runnoob.com'))
# 4、使用字典设置参数，需要**传递字典
dic = {'name': 'runnoob', 'url': 'www.runnoob.com'}
print('网站名：{name}，地址：{url}'.format(**dic))
# 5、使用列表设置参数
li = ['runnoob', 'www.runnoob.com']
print('网站名：{0[0]}，地址：{0[1]}'.format(li))
li2 = ['菜鸟教程', 'admin']
print('网站名：{0[0]}，地址：{0[1]}。用户名：{1[0]}，权限：{1[1]}。'.format(li, li2))
