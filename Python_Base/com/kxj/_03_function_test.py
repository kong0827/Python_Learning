# 导入文件，不能以数字开头
from Python_Base.com.kxj._03_function import my_abs, nop, my_abs2, move, enroll
import math

print(my_abs(10))
print(nop())

# 参数检查
# print(my_abs(1, 2))
# print(my_abs('a'))

# 抛出自定义异常
# print(my_abs2('1'))

# 接收多个值, 实际上返回的是一个tuple(元组)
x, y = move(1, 2, 60, math.pi * 6)
print(x, y)
r = move(1, 2, 60, math.pi * 6)
print(r)

# 默认参数调用
enroll('zhangsan', '男')
enroll('lisi', '女', 18)
enroll('wanger', '男', 20, '南京')
enroll('azhang', '男', city='合肥')

