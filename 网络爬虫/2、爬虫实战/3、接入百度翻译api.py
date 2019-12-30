#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib

appid = '20190323000280309'
secret_key = 'FE0bKiSX6g8UjZ8tjg0v'
api_url = 'https://fanyi-api.baidu.com/api/trans/vip/translate'


def translate(word):
    parameters = {
        'q' = word,
        'from' = 'en',
        'to' = 'zh',
        'appid' = appid
    }
