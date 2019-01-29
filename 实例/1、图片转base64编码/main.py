#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import base64

while True:
    image = input('请拖拽想要处理的文件到窗口中！\n')

    with open(image, 'rb') as img:
        img_b64 = base64.b64encode(img.read())

    with open('main\\result.txt', 'w') as res:
        b64_str = str(img_b64)[2: -1]
        res.write(b64_str)

    os.system('main\\result.txt')
    input('回车键继续，Ctrl+C退出')
    print('-' * 60)
