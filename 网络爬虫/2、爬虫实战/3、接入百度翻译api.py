#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib

appid = ''  # ID
secret_key = ''  # 密码
api_url = 'https://fanyi-api.baidu.com/api/trans/vip/translate'


def translate(word):
    parameters = {
        'q' = word,
        'from' = 'en',
        'to' = 'zh',
        'appid' = appid
    }
