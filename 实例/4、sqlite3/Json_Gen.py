'''
Author: MK_Devil
Date: 2022-01-13 11:13:09
LastEditTime: 2022-01-14 17:33:09
LastEditors: MK_Devil
'''
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sqlite3
import json
import lib

# data_file = open('data.json', 'r+')
con = sqlite3.connect('Alchemy.db')
cur = con.cursor()

cur.execute("SELECT * FROM material")
get_sql_data = cur.fetchall()

# 获取所有名称
mat_name = []
for x in get_sql_data:
    mat_name.append(x[0])
print(mat_name)

# 获取所有效果
mat_effect = []
for x in get_sql_data:
    for y in range(2, 5):
        mat_effect.append(x[y])
print(lib.del_repeat(mat_effect))

json_data = {'mat_name': mat_name, 'mat_effect': mat_effect}
with open('data.json', 'r+') as data_file:
    json.dump(json_data, data_file)
with open('data.json', 'r') as data_file:
    json_data = json.load(data_file)
    print(json_data)
# 关闭数据库连接
con.commit()
con.close()
