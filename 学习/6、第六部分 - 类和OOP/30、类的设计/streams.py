#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 重访流处理器


class Processor(object):
    def __init__(self, reader, writer):
        self.reader = reader
        self.writer = writer

    def process(self):
        while 1:
            data = self.reader.readline()
            if not data:
                break
            data = self.converter(data)
            self.writer.write(data)

    def converter(self, data):
        assert False, 'converter must be defined.'
