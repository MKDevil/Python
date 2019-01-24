#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 示例一、计数器---------------------------------------------------------------
print('\n', '-' * 30, '    示例一、计数器    ', '-' * 30)


def counter(start=0):
    status = start

    def times():
        nonlocal status
        status += 1
        return status
    return times


c1 = counter()
for i in range(5):
    print(c1())

c2 = counter(20)
for i in range(4):
    print(c2())

# 示例二、计数器（使用类编写）-------------------------------------------------
print('\n', '-' * 30, '    示例二、计数器（使用类编写）    ', '-' * 30)


class Counter():
    def __init__(self, start=0):
        self.state = start

    def __call__(self, label):
        """重写__call__方法，使类的调用看起来更像一个函数"""
        print(label, self.state)
        self.state += 1


c1 = Counter()
for i in 'spam':
    c1(i)

c2 = Counter(20)
for i in 'fantasy':
    c2(i)
c1('fff')

# 示例三、移动-----------------------------------------------------------------
print('\n', '-' * 30, '    示例二、移动    ', '-' * 30)


def moveitem(start_pos=[0, 0]):
    status = start_pos

    def move(step, direction):
        nonlocal status
        if not isinstance(step, int):
            print('步数必须为整数！')
        elif direction not in [1, 2, 3, 4]:
            print('方向必须为数字！上(1)，下(2)，左(3)，右(4)')
        elif direction == 1:
            status[1] += step
        elif direction == 2:
            status[1] = + step
        elif direction == 3:
            status[0] -= step
        elif direction == 4:
            status[0] += step
        return status
    return move


a = moveitem()
print(a(20, 1))
print(a(10, 3))

# 示例四、移动（使用类编写）-----------------------------------------------------------------
print('\n', '-' * 30, '    示例二、移动（使用类编写）    ', '-' * 30)


class MoveItem():
    def __init__(self):
        self.move_direction = None
        self.move_step = None
        self.coor_x = 0
        self.coor_y = 0

    def move(self, step, direction):
        if not isinstance(step, int):
            print('步数必须为整数！')
        elif direction not in [1, 2, 3, 4]:
            print('方向必须为数字！上(1)，下(2)，左(3)，右(4)')
        elif direction == 1:
            self.move_direction = '上'
            self.move_step = step
            self.coor_y += step
        elif direction == 2:
            self.move_direction = '下'
            self.move_step = step
            self.coor_y -= step
        elif direction == 3:
            self.move_direction = '左'
            self.move_step = step
            self.coor_x -= step
        elif direction == 4:
            self.move_direction = '右'
            self.move_step = step
            self.coor_x += step
        print('物体向{move_direction}移动了{move_step}步，当前坐标为[{coor_x},{coor_y}]'.format(
            **self.__dict__))


b = MoveItem()
b.move(20, 3)
b.move(18, 2)
