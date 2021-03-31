tmp = list(range(0, 10))
print(tmp)

L = []
for x in range(1, 11):
    L.append(x * x)
print(L)

# 替代上面繁琐的代码
L = [x * x for x in range(1, 11)]
print(L)

# 生成偶数
L = [x * x for x in range(1, 11) if x % 2 == 0]
print(L)
