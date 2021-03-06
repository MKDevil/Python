#!/usr/bin/env python
# -*- coding:utf-8 -*-

# ----------------------------------------------------
# --------------------    引用    --------------------
# ----------------------------------------------------
# 如果两个对象引用了同一个对象，那么当被引用的对象改变的时候，两个引用它的对象也会改变
print('-' * 54)
print('-' * 20, '    引用    ', '-' * 20)
print('-' * 54)
dic1 = [1, 2, 3]
set1 = ('a', dic1, 'c')
set2 = ('e', dic1, 'f')
dic1[1] = 'faq'
print("dic1的内容为：\t{}\nset1的内容为：\t{}\nset2的内容为：\t{}\n".format(dic1, set1, set2))
set1[1][1] = 'curse'
print(dic1, set2)
print("dic1的内容为：\t{}\nset1的内容为：\t{}\nset2的内容为：\t{}\n".format(dic1, set1, set2))

# 可以通过查询对象的内存ID，来确认是否指向同一个内存位置
print('id(dic1)    = {}\nid(set1[1]) = {}\nid(set2[1]) = {}'.format(
    id(dic1), id(set1[1]), id(set2[1])))
print('可以看到，三个对象的指针都指向同一个位置。')

# ----------------------------------------------------
# --------------------    拷贝    --------------------
# ----------------------------------------------------
# 如果不想出现上面的情况，可以在赋值的时候进行拷贝
# 字符串，字符串不可以原地修改，因此不需要拷贝
# 列表 1、分片表达式L[:]可以生成一个新的序列
#      2、list.copy() 可以拷贝序列
# 字典 dict.copy() 可以拷贝字典
# copy 标准库模块
print('-' * 54)
print('-' * 20, '    拷贝    ', '-' * 20)
print('-' * 54)
dic1 = [1, 2, 3]
set1 = ('a', dic1.copy(), 'c')
set2 = ('e', dic1.copy(), 'f')
dic1[1] = 'faq'
print("dic1的内容为：\t{}\nset1的内容为：\t{}\nset2的内容为：\t{}\n".format(dic1, set1, set2))
set1[1][1] = 'curse'
print(dic1, set2)
print("dic1的内容为：\t{}\nset1的内容为：\t{}\nset2的内容为：\t{}\n".format(dic1, set1, set2))
print('id(dic1)    = {}\nid(set1[1]) = {}\nid(set2[1]) = {}'.format(
    id(dic1), id(set1[1]), id(set2[1])))
print('可以看到，三个对象的指针各自指向不同位置。')

# ----------------------------------------------------
# --------------------    比较    --------------------
# ----------------------------------------------------
# == 测试一致性，递归的比较所有内嵌对象
# is 测试相等性，是否是同一个对象（位于同一个内存地址中）
print('-' * 54)
print('-' * 20, '    比较    ', '-' * 20)
print('-' * 54)

# 字符串，python自动将其储存在同一个内存地址中
str1 = 'spam'
str2 = 'spam'
print(str1 == str2, str1 is str2)
print('{}\t{}'.format(id(str1), id(str2)))

# python 中比较的方法
# 数字         按照相对大小比较
# 字符串       按字典顺序，即 ord() 后的结果，一个接一个字符进行比较
# 列表、元组   从左到右每个部分进行比较
# 字典         字典无法直接比较，但可以比较两个字典的 dict.items()

# bool() 方法，获得一个bool值

# type() 获取一个对象的类型
# isinstance(obj, class) 判断obj是否为类型class
