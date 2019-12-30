#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
通过使用浏览器的“审查元素”功能，其中的 network 可以查看网页在请求数据时发送和接收了哪些数据
GET：从服务器请求获取数据
POST：向指定服务器提交被处理的数据
"""

import urllib.request
import urllib.parse
import json

# url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'  # 去掉 _o
data = {}
data['i'] = 'fuck you'
data['from'] = 'AUTO'
data['to'] = 'AUTO'
data['smartresult'] = 'dict'
data['client'] = 'fanyideskweb'
data['salt'] = '15649771276210'
data['sign'] = '2bb3ce093644dcf0ba07e2760a239a43'
data['ts'] = '1564977127621'
data['bv'] = '53539dde41bde18f4a71bb075fcf2e66'
data['doctype'] = 'json'
data['version'] = '2.1'
data['keyfrom'] = 'fanyi.web'
data['action'] = 'FY_BY_CLICKBUTTION'

data = urllib.parse.urlencode(data).encode('utf-8')

response = urllib.request.urlopen(url, data)
html = response.read().decode('utf-8')
print(html)

target = json.loads(html)

src = target['translateResult'][0][0]['src']
tgt = target['translateResult'][0][0]['tgt']

print('元数据：%s\n翻译结果：%s' % (src, tgt))
