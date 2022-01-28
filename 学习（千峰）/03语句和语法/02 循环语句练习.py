'''
Author: MK_Devil
Date: 2021-12-20 17:18:09
LastEditTime: 2022-01-19 17:13:00
LastEditors: MK_Devil
'''
#!/usr/bin/env python
# -*- coding:utf-8 -*-

import random

# 打印 1-50 内可以被 3 整除的数字
n = 1
while n <= 50:
    if n % 3 == 0:
        print(n, end='\t')
    n += 1
print()

n = 1
counter = 1
while n + 3 < 50:
    n = 3 * counter
    counter += 1
    print(n, end='\t')
print()

# 打印 1-10 的累加和
n = 1
res = 0
while n <= 10:
    res += n
    n += 1
print(res)

# 猜数字

ran = random.randint(1, 50)
counter = 0
while True:
    guess = input('输入你猜的数字，输入 q 退出：')
    if guess == 'q':
        break
    guess = int(guess)
    counter += 1
    if guess > ran:
        print('大了')
    elif guess < ran:
        print('小了')
    else:
        print('正确，数字为%d' % ran)
        if counter == 1:
            print('恭喜一次猜对！')
        elif 1 < counter < 5:
            print('运气不错，%d次猜对' % counter)
        elif 5 < counter < 10:
            print('运气一般，%d次猜对' % counter)
        else:
            print('尼哥就是说的你，%d次才猜对' % counter)
        break
