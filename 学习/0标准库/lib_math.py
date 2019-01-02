#!/usr/bin/env python
# -*- coding:utf-8 -*-

import math

###################################      数学常数      ###################################
print('π = ', math.pi)    # 圆周率π
print('e = ', math.e)    # 自然常数e
print('τ = ', math.tau)    # 数字常数τ
print('正负无穷：', math.inf, -math.inf, '\n')    # 正负无穷

###################################      数论和表示函数      ###################################
# fsum() 求和，比sum更精确
fsum_num = [1, 2, 3, 4]
print('math.fsum = ', math.fsum(fsum_num))
print('sum = ', sum(fsum_num), '\n')

# fabs(x) 绝对值，同 abs()
print('fabs(-10) = ', math.fabs(-10))
print('abs(-10) = ', abs(-10), '\n')

# factorial(x) 阶乘x
print('factorial(4) = ', math.factorial(4), '\n')

# modf(x) 返回x的小数部分和整数部分
print('modf(-2.56) = ', math.modf(-2.56), '\n')

# copysign(x, y) 返回一个浮点数，绝对值x，符号y
print('copysign(2.56, -5) = ', math.copysign(2.56, -5), '\n')

# gcd(x, y) 求最大公约数
print('gcd(388, 658388) = ', math.gcd(388, 658388), '\n')

# frexp(x) 把一个浮点数拆分为尾数 a 和指数 b，返回(a，b)，x = a * (2 ** b)
# ldexp(a, b) 用尾数 a 和指数 b 重新返回为x
frexp_res = math.frexp(5.66)
print('frexp(5.66) = ', frexp_res)
print('ldexp() = ', math.ldexp(frexp_res[0], frexp_res[-1]), '\n')

# x / y = z ...... r 求余数
# fmod(x, y) 求余数，使 z 更接近于 0
# % 求余数，使 y * z < x
# remainder(x, y) 求余数，使 y * z 最接近 x
print('fmod(-5.2, 2) = %.2f \t fmod(5.2, 2) = %.2f' %
      (math.fmod(-5.2, 2), math.fmod(5.2, 2)))
print('-5.2 %% 2 = %.2f \t 5.2 %% 2 = %.2f' % (-5.2 % 2, 5.2 % 2))
print('remainder(-5.2, 2) = %.2f \t remainder(5.2, 2) = %.2f \n' %
      (math.remainder(-5.2, 2), math.remainder(5.2, 2)))

# 截断
# ceil(x) 取上限
# floor(x) 取下限，同 // 除法
# trunc(x) 去掉小数部分
print('ceil(-5.2) = %d \t ceil(5.2) = %d' % (math.ceil(-5.2), math.ceil(5.2)))
print('floor(-5.2) = %d \t floor(5.2) = %d' %
      (math.floor(-5.2), math.floor(5.2)))
print('trunc(-5.2) = %d \t trunc(5.8) = %d' %
      (math.trunc(-5.2), math.trunc(5.8)))
print('5.2 // 2 = %.1f \t 5.8 // 2 = %.1f \n -5.2 // 2 = %.1f \t -5.8 // 2 = %.1f \n' %
      (5.2 // 2, 5.8 // 2, -5.2 // 2, -5.8 // 2))

# isclose(x, y, rel_tol = 百分比精度, abs_tol = 绝对精度)
# 判断是否相近
print('isclose(900, 980, rel_tol = 0.1)：', math.isclose(900, 980, rel_tol=0.1))
print('isclose(900, 980, abs_tol = 80)：', math.isclose(900, 980, abs_tol=80))

# infinite(x) 判断是否为正常数字（不是 inf、NaN 或其他错误类型）
# isinf(x) 判断是否为正负无穷
# isnan(x) 判断是否为NaN
