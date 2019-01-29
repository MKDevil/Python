#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import base64

with open(sys.argv[1], 'rb') as img:
    img_b64 = base64.b64encode(img.read())

with open('main\\result.txt', 'w') as res:
    b64_str = str(img_b64)[2: -1]
    res.write(b64_str)
