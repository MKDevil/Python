#!/usr/bin/env python
# -*- coding:utf-8 -*-
import urllib.request

# req = urllib.request.Request('http://placekitten.com/g/500/600')
# response = urllib.request.urlopen(req)
# 这是一种较为复杂的写法，先创建一个 Request 类，然后读取这个类

response = urllib.request.urlopen('http://placekitten.com/g/500/600')
cat_img = response.read()

with open('.result/cat_500_600.jpg', 'wb') as file:
    file.write(cat_img)

print(response.geturl())
print(response.info())
print(response.getcode())
