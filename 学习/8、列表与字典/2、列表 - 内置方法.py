#!/usr/bin/env python
# -*- coding:utf-8 -*-
s = ['a', 'c', 'b', 'c']

# copy() 复制列表
a = s.copy()
print("a = s.copy()：\n\t", a)

# -------------------------    查询    -------------------------
# count(obj) 计算某个元素 obj 在列表中出现的次数
print("元素'c'在列表中出现的次数为：\n\t", s.count('c'))

# index(obj) 查询某个元素 obj 在列表中第一次出现的位置
print("元素'c'在列表中第一次出现的位置为：\n\t", s.index('c'))

# -------------------------    排序    -------------------------
# sort(key=None, reverse=False) 排序
# key 用来比较的元素
# reverse 排序规则，默认False 升序，True 降序
s.sort(reverse = True)
print("s.sort(reverse = True)：\n\t", s)

# reverse() 反向排列
s.reverse()
print("s.reverse()：\n\t", s)

# -------------------------    添加    -------------------------
# append() 在列表末尾添加新的对象
s.append('d')
print("s.append('d')：\n\t", s)
s.append(['e', 'c'])
print("s.append(['e', 'c'])：\n\t", s)

# extend(list2) 在列表末尾一次性追加另一个序列中的多个值
# 等同于 list1 + list2
s.extend(['f', 'c'])
print("s.eobjtend(['f', 'c'])：\n\t", s)

# insert(index, obj) 在偏移为index的位置插入元素obj
s.insert(3, 'faq')
print("s.insert(3, 'faq')：\n\t", s)

# -------------------------    删除    -------------------------
# remove(obj) 移除列表中第一个obj元素
s.remove('c')
print("s.remove('c')：\n\t", s)

# pop(index) 移除列表中偏移为 index 的元素，并返回该元素的值，默认-1
print("s.pop(-2)：\n\t", s.pop(-2))
print("s.pop()：\n\t", s.pop())
print(s)

# clear() 清空列表，等同于del listname[:]
s.clear()
print("s.clear()：\n\t", s)
