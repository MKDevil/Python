'''
Author: MK_Devil
Date: 2022-01-13 11:13:09
LastEditTime: 2022-01-14 14:13:31
LastEditors: MK_Devil
'''
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sqlite3

# 建立数据库连接
conn = sqlite3.connect(r'.\实例\4、sqlite3\Alchemy.db')

# 创建游标
cur = conn.cursor()
# 查询输出所有
# cur.execute(r'select * from material')
# print(cur.fetchall())
