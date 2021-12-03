'''
Author: MK_Devil
Date: 2021-09-09 17:00:55
LastEditTime: 2021-12-01 16:43:51
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
movie = '皮卡丘'
ticket = 45.97
count = 35
total = ticket * count
print('电影：%s\n人数：%s\n总价：%.1f' % (movie, count, total))

############################## format 方法 ##############################
print('电影：{}\n人数：{}\n总价：{}'.format(movie, count, total))
