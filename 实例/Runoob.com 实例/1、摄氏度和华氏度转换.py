#!/usr/bin/env python
# -*- coding:utf-8 -*-


def CtoF(celsius):
    return celsius * 1.8 + 32


def FtoC(fahrenheit):
    return (fahrenheit - 32) / 1.8


while True:
    temperature = input('输入华氏度或摄氏度，并使用大写的F或C结尾，如18C\n按Ctrl+C退出程序\n')
    if temperature[-1] == 'C':
        print('%s = %sF' % (temperature, CtoF(float(temperature[:-1]))))
    else:
        print('%s = %sC' % (temperature, FtoC(float(temperature[:-1]))))
    input('任意键继续，退出请按Ctrl+C')
