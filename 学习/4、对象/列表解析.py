
# 列出1-10所有数字的平方
# 方法1
num1 = []
for i in range(1, 11):
    num1.append(i ** 2)
print('num1:', num1)

# 方法2
num2 = [i**2 for i in range(1, 11)]
print('num2:', num2)


# 列出1-10中大于等于4的数字的平方
# 方法1
num3 = []
for i in range(1, 11):
    if i >= 4:
        num3.append(i ** 2)
print('num3:', num3)

# 方法2
num4 = [i ** 2 for i in range(1, 11) if i >= 4]
print('num4:', num4)

# 二维数组
M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
N = [i[1] for i in M]
print('M:', M, '\t', 'N:', N)
K = [M[i][j] for i in range(0, 3) for j in range(1, 3)]
print('K:', K)
L = (sum(k) for k in M)
print('next(L):', next(L))
print('next(L):', next(L))
print('next(L):', next(L))
L1 = list(map(sum, M))
print('L1:', L1)
# 创建列表L2
L2 = [ord(i) for i in 'fuck']
print('L2：', L2)
# 创建集合J1
J1 = {sum(i) for i in M}
print('J1:', J1)
# 创建字典D1，D2
D1 = {i: sum(M[i]) for i in range(0, 3)}
D2 = {i: ord(i) for i in 'fuck'}
print('D1:', D1, '\nD2：', D2)
