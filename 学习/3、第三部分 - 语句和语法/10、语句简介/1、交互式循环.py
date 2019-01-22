#!/usr/bin/env python
# -*- coding:utf-8 -*-

while True:
    content = input('enter text:')
    if content == '':
        print('bye')
        break
    elif content.isdigit():
        num = int(content)
        if num < 20:
            print('a lower num!')
        else:
            print(num ** 10)
    else:
        print('Error!')
