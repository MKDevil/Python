'''
Author: MK_Devil
Date: 2021-12-17 16:47:24
LastEditTime: 2021-12-20 17:09:30
LastEditors: MK_Devil
'''
#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
输入单价        int
输入商品数量    float
计算总价
提示4种付款方式:
    现金：无折扣
    微信：95折
    支付宝：随机立减1~5元
    刷卡：满100-20
'''
import random

price = float(input('输入单价：\n'))
count = int(input('输入数量：\n'))
total = price * count
choice = input('商品总价：%.2f元\n输入数字选择您的支付方式：\n1、现金\n2、微信\n3、支付宝\n4、刷卡\n' % total)

if choice == '1':
    print('现金支付：%.2f元' % total)
elif choice == '2':
    total *= 0.95
    print('微信支付：%.2f元' % total)
elif choice == '3':
    coupon = random.uniform(0, 5)
    total -= coupon
    print('支付宝支付：%.2f元\n本次优惠%.2f元' % (total, coupon))
elif choice == '4':
    coupon = total // 100 * 20
    total -= coupon
    print('刷卡支付：%.2f元' % total)
else:
    print('Error!!!!')
