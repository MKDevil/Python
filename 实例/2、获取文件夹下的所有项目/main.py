#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
"""
workdir = os.getcwd() + r'\work'
print(workdir)
for root, dirs, files in os.walk(workdir):
    files = files
print(files)

with open('res.md', 'w', encoding='utf-8') as f:
    f.write('|序号|名称|\n|-|-|\n')
    for filenameandorder in files:
        order = filenameandorder[0: 2]
        filename = filenameandorder[2: -4]
        f.write('|`' + order + '`|')
        f.write(filename + '|\n')
os.system('res.md')
"""

workdir = os.getcwd() + r'\work'
for i, j, k in os.walk(workdir):
    get_files = k

num_list = []
name_list = []
for name_num in get_files:
    num_list.append(name_num[0: 2])
    name_list.append(name_num[2: -4])
print(name_list)
print(num_list)

if len(get_files) % 2 == 0:
    table_row_num = len(get_files) / 2
elif len(get_files) % 2 == 1:
    table_row_num = len(get_files) // 2 + 1
table_row_num = int(table_row_num)
with open('res.md', 'w', encoding='utf-8') as f:
    f.write('|序号|名称|序号|名称|\n|-|-|-|-|\n')
    i = 0
    while i < table_row_num:
        f.write('|`' + num_list[i] + '`|' + name_list[i])
        try:
            f.write('|`' + num_list[i + table_row_num] +
                    '`|' + name_list[i + table_row_num] + '|\n')
        except IndexError:
            break
        i += 1
os.system('res.md')
