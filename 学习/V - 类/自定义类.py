
# 自定义人员信息


class Worker():
    """docstring for Worker"""

    def __init__(self, name, sex, old, depart):
        super(Worker, self).__init__()
        self.name = name
        self.sex = sex
        self.old = old
        self.depart = depart

    def move(self, move_depart):
        self.depart = move_depart
        print(self.name, '调入', move_depart)
        print('%s 调入 %s ！！！！！' % (self.name, move_depart))


w1 = Worker('渣渣辉', '男', 24, '贪玩蓝月')
w2 = Worker('古天乐', '男', 27, '贪玩蓝月')
w3 = Worker('谢霆锋', '男', 24, '贪玩蓝月')
print(w1.name, w1.sex, w1.old, w1.depart)
print(w2.name, w2.sex, w2.old, w2.depart)
print(w3.name, w3.sex, w3.old, w3.depart)
w3.move('蓝月传奇')
print(w3.name, w3.sex, w3.old, w3.depart)

print(dir(w1))
print(w1.__class__)
