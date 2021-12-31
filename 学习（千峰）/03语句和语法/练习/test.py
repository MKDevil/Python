'''
Author: MK_Devil
Date: 2021-12-20 17:18:09
LastEditTime: 2021-12-20 17:22:54
LastEditors: MK_Devil
'''
#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 打印 1-50 内可以被 3 整除的数字
n = 1
while n <= 50:
    if n % 3 == 0:
        print(n, end='\t')
    n += 1

# 打印 1-10 的累加和
n = 1
res = 0
while n <= 10:
    res += n
    n += 1
print(res)
