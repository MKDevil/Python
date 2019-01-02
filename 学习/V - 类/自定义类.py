
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


w1 = Worker('孟令珂', '男', 24, '村镇科')
w2 = Worker('续恒州', '男', 27, '市政科')
w3 = Worker('张少康', '男', 24, '办公室')
print(w1.name, w1.sex, w1.old, w1.depart)
print(w2.name, w2.sex, w2.old, w2.depart)
print(w3.name, w3.sex, w3.old, w3.depart)
w3.move('编制科')
print(w3.name, w3.sex, w3.old, w3.depart)

print(dir(w1))
print(w1.__class__)
