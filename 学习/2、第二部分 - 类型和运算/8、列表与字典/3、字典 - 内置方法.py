#!/usr/bin/env python
# -*- coding:utf-8 -*-
stu = {'name': 'Alice', 'age': 20, 'grade': 88}


# -------------------------    特殊方法    -------------------------
# copy() 复制字典
stu2 = stu.copy()
print('stu2 = stu.copy()\n\t%s\n' % stu2)

# fromkeys(keys, value) 按照键值生成一个字典
# value的值只有一个，且会被赋值到每一个键
keys = ['name', 'age', 'grade']
values = ['Mike', 20, 88.7]
stu2 = dict.fromkeys(keys, values)
print('使用fromkeys生成一个字典！dict.fromkeys(keys,values)\n\t', stu2)
# 当对生成的某一个字典的值进行append操作时，所有键的值都会改变
stu2['name'].append('faq')
print('当对生成的某一个字典的值进行append操作时，所有键的值都会改变！\n\t', stu2)
# 但是直接更改值是可以的
stu2['age'] = [24, 25]
print('但是直接更改值是可以的！\n\t', stu2)
# 这种方式可以形成一种“连坐”的效果，特殊情况下困难会有奇效

# 如果想生成对应键值的字典，采用zip方式进行
stu3 = dict(zip(keys, values))
print('使用zip方法生成一个字典：\n\t%s\n' % stu3)


# -------------------------    查询    -------------------------
# keys() 获取所有键值，返回一个相应的列表
print('stu中的键有：\n\t', stu.keys())

# values() 获取所有的值，返回一个相应的列表
print('stu中的值有：\n\t', stu.values())

# items() 获取所有的键和对应值，每个键和值组成一个元组，再组成一个列表
print('stu中的元素有：\n\t', stu.items())

# get(key) 获取某个键对应的值，如果没有该键，就返回 None
print("stu.get('name')\n\t%s\n" % stu.get('name'))


# -------------------------    添加    -------------------------
# setdefault(key[, default = None]) 查询/添加一个键/值
# 如果存在对应的key，则获得key的值
# 如果不存在对应的key，则添加一个新的key，并为其赋default位置的值
print('stu3使用default查询键name\n\t', stu3.setdefault('name'))
print('stu3使用default添加键greet\n\t', stu3.setdefault('greet'))
print('stu3使用default添加键alert，键值为warning\n\t',
      stu3.setdefault('alert', 'warning'))
print('修改过后的stu3为\n\t%s\n' % stu3)

# update(dict2) 将字典dict2的键和值添加到字典中，重复键会覆盖
dict2 = {'from': 'America', 'livein': 'shanghai', 'name': 'Jerry'}
stu.update(dict2)
print('dict2的内容为\n\t%s\n将dict2的内容添加到stu中\n\t%s\n' % (dict2, stu))


# -------------------------    删除    -------------------------
# pop(key[, default]) 删除并返回key对应的值，查找不到key则返回default值
print('删除stu中的livein键并返回\n\t%s' % stu.pop('livein'))
print('删除stu中的country键并返回默认值\n\t%s\n' % stu.pop('country', '没有查询到键'))

# popitem() 随机删除并返回字典的键和对应的值，一般删除最后一项
print('随机删除stu中的一对键值\n\t%s:%s' % stu.popitem())
print('随机删除stu中的一对键值\n\t%s:%s' % stu.popitem())

# clear() 清空
stu.clear()
