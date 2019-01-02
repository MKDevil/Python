#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 类的定义，object表示为父类


class Bird(object):
    have_feather = True
    way_of_reproduction = 'egg'
    # 定义类的方法

    def move(self, dx, dy):
        position = [0, 0]
        position[0] = position[0] + dx
        position[1] = position[1] + dy
        return position


summer = Bird()
print(summer.way_of_reproduction)
print(summer.move(5, 8))

# 定义子类


class Chicken(Bird):
    way_of_move = 'walk'
    possible_in_KFC = True


class Oriole(Bird):
    way_of_move = 'fly'
    possible_in_KFC = False

# 子类重写父类方法


class Small_Oriole(Bird):
    way_of_move = 'walk'


spring = Small_Oriole()
print(spring.way_of_move)

# __init__方法在建立对象时自动执行


class HappyBird(Bird):
    def __init__(self, more_words):
        print('we are happy birds.', more_words)


summer = HappyBird('happy,happy!')
