#!/usr/bin/env python
# -*- coding:utf-8 -*-


# 示例一、定义类--------------------------------------------------------
class FirstClass():
    def setdata(self, value):
        self.data = value

    def display(self):
        print(self.data)


x = FirstClass()
x.setdata(99)
y = FirstClass()
y.setdata(88)
x.display()
y.display()

# 可以直接给类实例增加新的没有定义过的属性
x.newvalue = 'New value'
print(x.newvalue)


# 示例二、类的继承------------------------------------------------------
class SecondClass(FirstClass):
    def display(self):
        print('Current value = %s' % self.data)


z = SecondClass()
z.setdata(77)
z.display()


# 示例三、运算符重载----------------------------------------------------
class ThirdClass(SecondClass):
    def __init__(self, data):
        """重写构造函数"""
        self.data = data

    def __add__(self, other):
        """
        重写 + 运算
        只适用于类实例在加号左边，否则会报错
        """
        return ThirdClass(self.data + other)

    def __str__(self):
        """重写 print 的方法"""
        return 'ThirdClass: %s' % self.data

    def mul(self, other):
        self.data *= other


a = ThirdClass('abc')
a.display()
print(a)
b = a + 'xyz'  # 实例 a 传递给 self，字符串 'xyz' 传递给 other
b.display()
print(b)
a.mul(3)
print(a)


# 示例四、最简单的类----------------------------------------------------
class rec:
    pass


# 这个类，没有实例，只存在命名空间
rec.name = 'Bob'
rec.age = 40
print(rec.name, rec.age)
x = rec()
print(x.name)
print(x.__dict__.keys())  # x 的 name 属性来自于 rec，x 自身并没有额外属性
x.name = 'Tom'
print(x.name)
print(x.__dict__.keys())
print(x.__class__)
print(rec.__dict__.keys())


# 示例五、在类外写方法--------------------------------------------------
def upper(self):
    return self.name.upper()


print(upper(x))
rec.method = upper  # 可以将外部写的方法，赋值给类
print(x.method())
