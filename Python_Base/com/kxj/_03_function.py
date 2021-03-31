import math


def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


def my_abs2(x):
    if not isinstance(x, (int, float)):
        raise TypeError('类型错误')
    if x >= 0:
        return x
    else:
        return -x


# 返回多个值
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


# 空函数
def nop():
    pass


# 默认参数
def enroll(name, gender, age=0, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)


#  定义默认参数要牢记一点：默认参数必须指向不变对象！
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
