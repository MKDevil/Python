'''
Author: MK_Devil
Date: 2022-01-13 11:13:09
LastEditTime: 2022-01-14 11:51:42
LastEditors: MK_Devil
'''
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json
import
file_mat = open('material.txt', 'r+')
while True:
    get_str = input('输入名称，是否，四种数据，使用空格分隔，输入exit结束\n')
    if get_str == 'exit':
        break
    get_list = get_str.split(' ')
    print(get_list)
    save = input('是否保存y/n:')
    if save == 'y':
        pass  # 添加json数据
