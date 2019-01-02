#!/usr/bin/env python
# -*- coding:utf-8 -*-

import random

###################################      簿记功能      ###################################
# seed(x, [version = y]) 设置一个种子，相同的种子随机的结果相同
# y = 1 算法1
# y = 2 算法2，默认为2
random.seed('faqsdfsd')
print(random.random())
random.seed('faqsdfsd')
print(random.random())
random.seed('faqsdfsd')
print(random.random(), '\n')

# getstate() 返回一个当前生成器的内部状态的对象
# setstate() 传入一个先前利用getstate方法获得的状态对象，使得生成器恢复到这个状态
# 通过以上方法，可以将生成器回溯到某个状态，得到相同的结果

# getrandbits(x) 返回一个x位的二进制随机整数
print('随机生成二十个八位二进制整数（0~255）：')
bit8 = [random.getrandbits(8) for i in range(0, 20)]
print('二十次getrandbits(8)：', bit8, '\n')

###################################      整数函数      ###################################
# randrange([start], end, [step]) 返回指定序列中的随机数
randlist = [random.randrange(0, 10, 3) for i in range(0, 20)]
print('二十次randrange(0, 10, 3)：', randlist, '\n')

# randint(a, b) 返回 一个随机整数N，包括两端端点
randlist = [random.randint(1, 2) for i in range(0, 20)]
print('二十次randint：', randlist)

###################################      序列函数      ###################################
# choice() 从非空序列中返回一个随机元素
print('random.choice(range(1, 10) = ', random.choice(range(1, 10)))
print('random.choice(randlist) = ', random.choice(randlist), '\n')

# choices()

# shuffle(x) 随机进行序列排序，会修改原序列
print('randlist = ', randlist)
random.shuffle(randlist)
print('randlist重新排序：', randlist, '\n')

# sample(x, k) 可以从指定的序列中，随机的截取指定长度k的片断，不作原地修改
print('random.sample(randlist) = ', random.sample(randlist, len(randlist) // 3))

###################################      实值分配      ###################################
# random() 返回[0.0, 1.0)范围内的随机浮点数
randlist = [random.random() for i in range(0, 20)]
print('20次random.random：', randlist)

# uniform(a, b) 返回[a, b]范围内的随机浮点数
randlist = [random.uniform(0.8, 0.99) for i in range(0, 20)]
print('20次random.uniform：', randlist)

# triangular(low, high, mode) 三角分布的随机数，mode指明众数出现的位置
# betavariate(alpha, beta) β分布
# expovariate() 指数分布
# gammavariate() gamma分布
# gauss() 高斯分布
# lognormvariate() 对数正态分布
# normalvariate() 正态分布
# vonmisesvariate() 循环正态分布
# paretovariate() 帕雷托分布
# weibullvariate() 威布尔分布

###################################      替代方式      ###################################
# class random.SystemRandom([seed])
