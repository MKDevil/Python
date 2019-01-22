#!/usr/bin/env python
# -*- coding:utf-8 -*-
import fractions

a = fractions.Fraction(1, 3)
b = fractions.Fraction(4, 6)
print(a)
print(b)
print(a + b)
print(a - b)

c = fractions.Fraction('0.25')
print(c)

# float类型转fraction类型
d = 2.55
e = fractions.Fraction(*d.as_integer_ratio())
print('2.55.as_integer_ratio()后：\n\t', e)
print('fractions.Fraction(\'2.55\')：\n\t', fractions.Fraction('2.55'))
# 由于float类型的精度问题，任然存在精度损失
# 将最大分母值限制为10
print('限制分母最大值为20：\n\t', e.limit_denominator(20))
