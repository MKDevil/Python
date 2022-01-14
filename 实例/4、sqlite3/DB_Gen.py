'''
Author: MK_Devil
Date: 2022-01-13 11:13:09
LastEditTime: 2022-01-14 16:53:31
LastEditors: MK_Devil
'''
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sqlite3

# 建立数据库连接
con = sqlite3.connect('Alchemy.db')

# 创建游标
cur = con.cursor()

sql_str = "SELECT * FROM material WHERE "

# 提交修改并保存
# con.commit()
con.close()