#!/usr/bin/env python
# -*- coding:utf-8 -*-
import random

origin = [0, 0]  # 设定原点[0, 0]


def create(pos=origin):
    def move(direction, step):
        # new_x = pos[0] + direction[0]*step
        # new_y = pos[1] + direction[1]*step
        # pos = [new_x, new_y]  这种赋值的方式会报错
        pos[0] += direction[0] * step
        pos[1] += direction[1] * step
        print(pos)
        return pos
    return move


hu = create()
hu([0, 1], 10)
print('另一种实现方式！！！！！！！！！！！')

# 既然这样，我为什么不用类呢！！！！！！！！！！！！！！！
# 注意：下面的方法并非闭包


class Player(object):
    def __init__(self, name):
        self.name = name
        self.pos = [random.randint(-20, 20), random.randint(-20, 20)]
        print('%s的初始坐标为[%d, %d]' % (self.name, self.pos[0], self.pos[1]))

    def move(self, direction, step):
        if direction not in (1, 2, 3, 4):
            print('错误！输入的方向必须在(1, 2, 3, 4)之中！')
        elif isinstance(step, int) or isinstance(step, float):
            # 实现方式1---------------------------------------
            # def up(direction):
            #     self.pos[1] += step
            #     return self, '上'
            # def down(direction):
            #     self.pos[1] -= step
            #     return self, '下'
            # def left(direction):
            #     self.pos[0] -= step
            #     return self, '左'
            # def right(direction):
            #     self.pos[0] += step
            #     return self, '右'
            # operator = {1: up, 2: down, 3: left, 4: right}
            # move_res = operator[direction](direction)
            # print('%s向%s移动了%d步，移动后的坐标为[%d, %d]' % (self.name, move_res[1], step, self.pos[0], self.pos[1]))
            # 实现方式2---------------------------------------
            def up():
                tar_pos = self.pos[1] + step
                return self.pos[0], tar_pos, '上'

            def down():
                tar_pos = self.pos[1] - step
                return self.pos[0], tar_pos, '下'

            def left():
                tar_pos = self.pos[0] - step
                return tar_pos, self.pos[1], '左'

            def right():
                tar_pos = self.pos[0] + step
                return tar_pos, self.pos[1], '右'
                # 返回的self.pos[0]和self.pos[1]只在up()函数内有效，无法改变环境变量self的内容

            operator = {1: up(), 2: down(), 3: left(), 4: right()}
            move_res = operator[direction]
            # 返回的move_res变量是一个list，需要将list的前两项赋值给self对象对应的值
            self.pos[0] = move_res[0]
            self.pos[1] = move_res[1]
            print('%s向%s移动了%d步，移动后的坐标为[%d, %d]'
                  % (self.name, move_res[2], step, self.pos[0], self.pos[1]))
        else:
            print('错误！输入的步数必须为int或float！')


test = Player('testname')
test.move(1, 10)
test.move(3, 8)
