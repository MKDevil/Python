#!/usr/bin/env python
# -*- coding:utf-8 -*-

import http.client

conn = http.client.HTTPConnection('www.cnblogs.com')
conn.request('GET', '/vamei')
res = conn.getresponse()
content = res.read()
print(type(content))
print(content)
input()
