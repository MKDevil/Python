#!/usr/bin/env python
# -*- coding:utf-8 -*-

# break             跳出最近所在的循环
# continue          跳到最近所在循环的开头处（来到循环的首行）
# pass              占位语句，什么事也不做
# 循环else模块      只有当循环正常离开时才会执行（没有触发break）

# 示例，break
res = i = 0
while True:
    i += 1
    res += i
    if i == 100:
        break
print(res)

# 示例，continue
# 求1~100之内的奇数的和
res = i = 0
while i < 100:
    i += 1
    if i % 2 == 0:
        continue
    res += i
print(res)

# 示例，循环else模块
res = i = 0
while i < 100:
    i += 1
    res += i
else:
    print(res)

# 示例，判断质数
for y in range(2, 100):
    x = y // 2
    while x > 1:
        if y % x == 0:
            # print(y, 'has a factor:', x)
            break
        x -= 1
    else:
        print(y, '是一个质数')
