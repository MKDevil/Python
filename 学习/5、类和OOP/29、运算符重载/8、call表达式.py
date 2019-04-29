#!/usr/bin/env python
# -*- coding:utf-8 -*-
import tkinter


class CallBack(object):
    def __init__(self, color):
        self.color = color
    def __call__(self):
        print('turn:', self.color)


cb1 = CallBack('blue')
cb2 = CallBack('green')
B1 = tkinter.Button(command=cb1)
B2 = tkinter.Button(command=cb2)
cb1()
