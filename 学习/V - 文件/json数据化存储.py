#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json

# import fileStatus
# with open('test.json', 'w') as file:
#     fileStatus.isOpen(file)
#     content = input('输入你想要的内容：\n')
#     json.dump(content, file)
#     print('输入完毕！')
# fileStatus.isOpen(file)

# json提供两个过程，encoding和decoding
# encoding过程 把python对象转换为json字符串
# decoding过程 把json字符串转换为python对象

# ----------------------------------------    encoding    ----------------------------------------
# 序列化，python对象→json字符串
# dumps(obj, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw)
# 序列化存储
# dump(obj, fp, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw)
# --------------------    参数详解    --------------------
# fp 文件对象
# sort_keys 序列化时候是否对dict进行排序
# indent 缩进，对数据进行缩进、格式化输出
# separators 消除冗余字符，如空格等，从而减少网络传输的数据量
#     如果indent值为None，其默认值为(',', ':')
#     如果indent值不为None，默认值为(', ', ': ')存在空格
#     可以通过separators = (',', ':')消除空白字符
# ensure_ascii 默认值True，输出的所有非ASCII字符（如中文）都会被转义为 \uXXXX 的序列
# skipkeys 默认值False，如果dict的keys内的数据不是python的基本数据类型，就会报错TypeError
#          设置为True，则会跳过会报错的keys
# check_circular 默认值True，对容器类型进行循环引用检查
#                设置为False，不进行检查，可能会导致OverflowError
# allow_nan 默认值True，使用其JavaScript对应的值(NaN, Infinity, -Infinity)
# default 自定义对象方法，默认None，通过为其写入一个自定义转换函数，可以用json存储python自定义对象
# cls 没啥卯月，懒得翻译文件

# ----------------------------------------    decoding    ----------------------------------------
# 反序列化，json字符串→python对象
# loads(s, encoding=None, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)
# 反序列化读取
# load(fp, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)
# --------------------    参数详解    --------------------
# encoding 编码格式，仅loads()方法有用
# object_hook 自定义对象方法，默认None，通过为其写入一个自定义转换函数，可以将json解码为python自定义对象
# object_pairs_hook 是一个可选函数，将使用有序的对列表对解码的任何对象文字的结果进行调用。
#                   将使用object_pairs_hook的返回值而不是dict。
#                   此功能可用于实现自定义解码器。
#                   如果还定义了object_hook，则object_pairs_hook优先。
# parse_float 默认值None，如果指定了值，则解码每个json字符串中的float值。
#             可以让json float用另一种数据类型或解析器（如decimal.Decimal）
# parse_int   默认值None，如果指定了值，则解码每个json字符串中的int值。
#             可以让json int用另一种数据类型或解析器（如float)
# parse_constant 默认值None，如果指定了值，将使用以下字符串之一调用：Nan, Infinity, -Infinity
#                遇到无效的json符号时，可能会报错

js_ende = {
    'a': '你好',
    'c': True,
    'e': 10,
    'b': 11.1,
    'd': None,
    'f': [1, 2, 3],
    'g': (4, 5, 6)
}
js_en = json.dumps(js_ende, sort_keys=True, indent=4, separators=(',', ':'))
print('encoding...\n\t', js_en)
js_de = json.loads(js_en)
print('decoding...\n\t', js_de)
print('\t', js_ende)
print('van全一致！！！')

with open('test.json', 'w') as file:
    json.dump(js_ende, file)
    print('文件输入完毕')
with open('test.json', 'r') as file:
    js_de_file = json.load(file)
    print('文件读取完毕：\n\t', js_de_file)

# ----------------------------------------    实例    ----------------------------------------


# 一、自定义数据类型的序列化
class Student(object):
    def __init__(self, name, age, sno):
        self.name = name
        self.age = age
        self.sno = sno

    def __repr__(self):
        return 'Student [name: %(name)s, age: %(age)d, sno: %(sno)d]' % self.__dict__


st1 = Student('alice', 12, 5)
print('\n\nst1的内容为：\n\t', st1)


# 方法1、编写转换函数
def objtodict(obj):
    dic = {}
    dic['__class__'] = obj.__class__.__name__  # 获取类名'Student'
    dic['__module__'] = obj.__module__  # 获取模块名称'__main__'
    dic.update(obj.__dict__)
    return dic


def dicttoobj(dic):
    if '__class__' in dic:
        module_name = dic.pop('__module__')  # 获取模块名'__main__'
        class_name = dic.pop('__class__')  # 获取类的名'Student'
        # 将模块名'__main__'赋值给module，使其成为一个空的类（module）
        module = __import__(module_name)
        # 使用getattr将class_name赋值给module，生成一个带有名字的新的类class_
        class_ = getattr(module, class_name)
        args = dict((key, value)
                    for key, value in dic.items())  # 确定class_类需要的参数，做成一个字典args
        # 不用args，直接使用删除'__module__'和'__class__'键的dic字典也可以，更省事
        instance = class_(**args)  # 将参数传递给class_类，形成一个完整的类
    else:
        instance = dic
    return instance


# 序列化 转义后输出到json
with open('stu.json', 'w') as file:
    json.dump(objtodict(st1), file, indent=4)
    print('\nstu.json内容输入完毕！\n\t先转换后输出！\n')
# 序列化 定义default方法输出到json
with open('stu.json', 'w') as file:
    json.dump(st1, file, indent=4, default=objtodict)
    print('stu.json内容输入完毕！\n\t定义default方法后输出！\n')
# 反序列化
with open('stu.json', 'r') as file:
    content = json.load(file, object_hook=dicttoobj)
    print('读取完毕，stu.json的内容为：\n\t', content)
    print('获取的数据类型为：\n\t', type(content))


# 二、继承JSONEncoder和JSONDecoder实现子类
class MyJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        dic = {}
        dic['__class__'] = obj.__class__.__name__
        dic['__module__'] = obj.__module__
        dic.update(obj.__dict__)
        return dic


class MyJsonDecoder(json.JSONDecoder):
    def __init__(self):
        json.JSONDecoder.__init__(self, object_hook=self.dict2obj)

    def dict2obj(self, dic):
        if '__class__' in dic:
            class_name = dic.pop('__class__')
            module_name = dic.pop('__module__')
            module = __import__(module_name)
            class_ = getattr(module, class_name)
            instance = class_(**dic)
        else:
            instance = dic
        return instance


# 直接调用子类MyJsonEncoder的encode()方法进行序列化
my_encode = MyJsonEncoder().encode(st1)
print('使用MyJsonEncoder()的encode()方法序列化：\n\t', my_encode)
# 直接调用子类MyJsonDecoder的decode()方法进行反序列化
my_decode = MyJsonDecoder().decode(my_encode)
print('使用MyJsonDecoder()的decode()方法反序列化：\n\t', my_decode)
print('\t获取的对象类型为：', type(my_decode))

# cls参数，将子类作为cls参数传递给json.dump和json.load函数
my_encode = json.dumps(st1, cls=MyJsonEncoder)
print('将子类作为cls参数传递给json.dumps方法进行序列化：\n\t', my_encode)
my_decode = json.loads(my_encode, cls=MyJsonDecoder)
print('将子类作为cls参数传递给json.loads方法进行序列化：\n\t', my_decode)
print('\t获取的对象类型为：', type(my_decode))

# 继承JSONEncoder实现序列化时还有一个额外的作用
# 就是可以通过iterencode()方法把一个很大的数据对象分多次进行序列化
# 这对于网络传输、磁盘持久化等情景非常有用。
for chunk in MyJsonEncoder().iterencode(st1):
    print(chunk)
# 大数据对象序列化网络传输伪代码：
# for chunk in JSONEncoder().iterencode(bigobject):
# mysocket.write(chunk)

# ----------------------------------------------------------------------------------------------------
print('\n\n\n\n--------------------Unicode字符转义：--------------------')
str1 = '你好'
str2 = str1.encode('unicode_escape')
print('%s转义为Unicode字符为：%s' % (str1, str2))
str3 = str2.decode('unicode_escape')
print('%s解码得到：%s' % (str2, str3))
str4 = str2.decode('utf-8')
print('%s转义后的实际显示需要去掉\\\n\t结果为：%s' % (str1, str4))
