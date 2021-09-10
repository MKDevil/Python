'''
Author: MK_Devil
Date: 2021-09-09 17:00:55
LastEditTime: 2021-09-09 17:52:34
LastEditors: MK_Devil
'''
#!/usr/bin/env python
# -*- coding:utf-8 -*-

person = 'jack'
phone = '123456'
address = 'New York'

# %s 相当于对变量进行 str() 运算
print('收件人：%s\n号码：%s\n地址：%s' % (person, phone, address))

# 输出字典数据需要字典的键
dic = {'person': 'lily', 'phone': '22222', 'address': 'Beijing'}
print('收件人：%(person)s\n号码：%(phone)s\n地址：%(address)s' % dic)

# %d 整型   %f 浮点型
