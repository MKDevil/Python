#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 创建一个字典
D1 = {'name': '孟令珂', 'old': 24, 'sex': 'man'}
print(D1)
print(D1['name'])
D1['old'] += 1
print(D1['old'])

# 字典和列表的嵌套,并输出其中的一个数据
D2 = {'name': ['孟令珂', '续恒州', '张少康'], 'sex': [
    'man', 'man', 'man'], 'old': [24, 27, 24]}
print('字典D2的长度为：', len(D2))
D2['name'].append('测试')
D2['old'].append(200)
D2['sex'].append('man')
D2_sort = list(D2)          # 将D2转换为一个列表，从而获取D2中键的名称
for i in range(0, len(D2) + 1):
    print('第', i + 1, '人信息：')
    for name in D2_sort:
        print('\t', name, '：', D2[name][i])
uName = sorted([D2['name'][i] for i in range(0, len(D2['name']))])
print('姓名排序', uName)

# sorted排序
D3 = {'a': 3, 'b': 1, 'c': 2}
for key in sorted(D3):
    print(key, '=>', D3[key])

# 检测是否有对应键
D4 = {'name': ['孟令珂', '续恒州', '张少康'], 'sex': [
    'man', 'man', 'man'], 'old': [24, 27, 24]}
key = input('输入你想查找的键：\n')
if key in D4:
    print('“', key, '”在字典D4中')
else:
    print('“', key, '”不在字典D4中')
print('字典D4的内容为：', D4)

# 在字典中添加新的项目
# print('D4的键有', sorted(D4))
# D4_len_name = len(D4['name'])
# D4_len_sex = len(D4['sex'])
# D4_len_old = len(D4['old'])
# counter = 1
# while (len(D4['name']) < D4_len_name + 1 or len(D4['old']) < D4_len_old + 1 or len(D4['sex']) < D4_len_sex + 1) and counter < 10:
#     key = input('输入你想添加的键的名称：\n')
#     if key not in D4:
#         print('D4中没有“', key, '”这个键')
#     else
#         input('你想添加的内容')

di = {'animal': ['chicken, cow, duck'], 'plant': ['apple, peach']}
counter = 0
while counter < 4:
    print('di中的键有：', sorted(di))
    key = input('你想添加的key：\n')
    if key not in di:
        print('木得')
        counter += 1
    else:
        print('字典di中的', key, '键中已有的内容为：', di[key])
        di_add = input('输入你想添加的内容：\n')
        di[key].append(di_add)
        print('添加成功！\n字典di中的', key, '键中已有的内容为：', di[key])
        counter += 1
print('循环达到上限，终止。')

print('输出字典的所有键：', di.keys())
print('输出字典的所有值：', di.values())
print('输出字典的所有元素：', di.items())
del di['animal']
print('删除字典中的animal元素：', di)
print('清空字典：', di.clear())
