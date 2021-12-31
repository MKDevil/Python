'''
Author: MK_Devil
Date: 2021-08-26 10:43:40
LastEditTime: 2021-12-17 16:34:49
LastEditors: MK_Devil
'''
#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 闰年


def runnian(year):
    if year % 400 == 0:
        print('闰年')
    elif (year % 4 == 0) and (year % 100 != 0):
        print('闰年')
    else:
        print('不是闰年')


while True:
    try:
        year = input('输入年份，输入exit退出：\n')
        if year == 'exit':
            break
        year = int(year)
        runnian(year)
    except ValueError as e:
        print(e)
        print('请输入一个整数！')
