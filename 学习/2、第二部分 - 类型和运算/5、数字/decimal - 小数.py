#!/usr/bin/env python
# -*- coding:utf-8 -*-
import decimal

print('python中自带的float类型，存在着精度问题：\n\t', 0.1 + 0.1 + 0.2 - 0.3)
print('使用decimal.Decimal类型可以修正这种问题：\n\t',
      decimal.Decimal('0.1') + decimal.Decimal('0.1') + decimal.Decimal('0.2') - decimal.Decimal('0.3'))

# 设置全局精度
decimal.getcontext().prec = 4
print('设置全局精度后：\n\t', decimal.Decimal('1')/decimal.Decimal('7'))

# 临时精度，使用上下文管理器可以实现
with decimal.localcontext() as ctx:
    ctx.prec = 2
    print('临时精度设置为2后：\n\t', decimal.Decimal('1')/decimal.Decimal('7'))
