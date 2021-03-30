from collections import Iterable

# 字典迭代 - map
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key, d[key])
print('------------------')

# 迭代value
for value in d.values():
    print(value)

print('------------------')
# 迭代字符串
for char in "ABCD":
    print(char)

print('------------------')
# 判断是否是可迭代对象
isInstance = isinstance('abc', Iterable)
print(isInstance)

