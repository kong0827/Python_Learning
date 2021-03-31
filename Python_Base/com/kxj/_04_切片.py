L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

# 取前三个元素
# 方法一
print([L[0], L[1], L[2]])

# 方法二
r = []
# 循环带索引
for i, j in enumerate(L):
    if i < 3:
        r.append(j)
print(r)

# 方法三 索引0可省略
print(L[0:3])
print(L[:3])

L = list(range(100))
print(L[10:20])

# 每隔两个取一个数
print(L[10:20:2])

# 复制一个数组
L1 = L[:]
print(L1)



