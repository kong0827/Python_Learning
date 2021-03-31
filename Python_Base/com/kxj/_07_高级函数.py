# 高阶函数
from functools import reduce


def f(x):
    return x * x


# map 使用
r = map(f, range(0, 10))
print(list(r))

# list所有数字转为字符串
r = map(str, range(0, 10))
print(list(r))


# reduce 使用
def fn(x, y):
    return str(x) + str(y)


r = reduce(fn, [1, 2, 3, 4])
print(r)
