#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 使用python的random库，生成随机长度的包含数字和字母的字符串

import random
# 设置字符串长度
# strLen = 64


def randomStr(strLen):
    # 随机数字个数
    numLen = random.randint(0, strLen)
    # 随机字母个数
    letterLen = strLen - numLen
    nums = [chr(random.randint(48, 57)) for i in range(0, numLen)]
    letters = [chr(random.randint(65, 90)) for i in range(0, letterLen)]
    res = nums + letters
    random.shuffle(res)
    result = ''.join(i for i in res)
    return result


strLen = int(input('输入想要的字符串长度：'))
print(type(strLen))
print(randomStr(strLen))
