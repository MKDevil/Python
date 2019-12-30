#!/usr/bin/env python
# -*- coding:utf-8 -*-
import urllib.request

response = urllib.request.urlopen('https://bbs.nga.cn/')
html = response.read()
print(html)
print('-' * 40, '此处为二进制编码，需要根据网页编码进行解码', '-' * 40)
html = html.decode('gbk')
print(html)

# 还可以写入文件中
# with open('result.txt', 'w') as file:
#     file.write(html)
