
# 三种检测对象类型的方法
L = [1, 2, 3]

# 第一种
print(type(L) == type([]))

# 第二种
print(type(L) == list)

# 第三种
print(isinstance(L, list))
