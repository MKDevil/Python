# 字符串相关操作
s = 'fuckman'
# 字符串索引
print('索引输出：')
print(s[0], s[-1])
print(s[1:2])
print(s[:-1])
print(s[2:])
print(s[:])

# 字符串运算
a = s * 2
b = s + 'yooo!'
print('a =', a)
print('b =', b)

# 长度
print('字符串s的长度', len(s))

# 转换字符串
num = 1999
print('num*2的数字型输出：', num * 2)
print('num转换为字符串后的num*2输出：', str(num) * 2)

# 查找指定字母位置()
print('请输入你想从字符串s（fuckman）中查找的字符或字符串：')
find_str = input()
find_num = s.find(find_str)
if find_num == -1:
    print('未找到指定字符/字符串！')
if find_num != -1:
    print('查找的字符/字符串偏移为：', find_num)

# 替换字符/字符串
print('输入你想替换“man”的字符串！')
rep_str = input()
rep_res = s.replace('man', rep_str)
print('替换结果：', rep_res)

# 拆分字符串
space = '  fuck  you,\nman  !   \n\n\n'
print(space.split())

# 字符串大写
print(space.upper())

# 查看字符串是否为字母、数字
print(space.isalpha())
print(space.isnumeric())

# 去除空格
print(space)
print(space.rstrip())
print(space)

# Unicode字符转义
print('\n\n\n\n--------------------Unicode字符转义：--------------------')
str1 = '你好'
str2 = str1.encode('unicode_escape')
print('%s转义为Unicode字符为：%s' % (str1, str2))
str3 = str2.decode('unicode_escape')
print('%s解码得到：%s' % (str2, str3))
str4 = str2.decode('utf-8')
print('%s转义后的实际显示需要去掉\\\n\t结果为：%s' % (str1, str4))
