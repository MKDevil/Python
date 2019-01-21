#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time
# 示例，列表解析与迭代
li = [1, 2, 3, 4, 5]
# 方法一，列表解析
start = time.perf_counter()
res = [i + 10 for i in li]
end = time.perf_counter()
print('列表解析的结果：\n\t{}\n\t运行时间：{:.8f}'.format(res, end - start))
# 方法二，for循环迭代
start = time.perf_counter()
res = []
for i in li:
    res.append(i + 10)
end = time.perf_counter()
print('for循环的结果：\n\t{}\n\t运行时间：{:.8f}'.format(res, end - start))

# 示例，列表解析读取文件
# 方法一，使用 readlines() 方法（不推荐）
with open('test.txt', 'r', encoding='utf-8') as f:
    content = f.readlines()
content_strip = [line.strip() for line in content]
print(content_strip)
# 方法二，在解析中打开文件
content_strip = [line.strip()
                 for line in open('test.txt', 'r', encoding='utf-8')]
print(content_strip)
# 方法三，直接迭代文件对象
with open('test.txt', 'r', encoding='utf-8') as f:
    content_strip = [line.strip() for line in f]
print(content_strip)

# 示例，增加 if 条件的列表解析！！！！！！！！！！！！！！！！！！！！！！！！！！！！
with open('2、手动迭代 - iter和next.py', 'r', encoding='utf-8') as f:
    content = [line.strip().upper() for line in f if line.strip() != '']
    content_p = [line for line in content if line[0] == 'P']
print(content_p)
