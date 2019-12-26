#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
def f(x):
    return x * x
r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
# list()函数让它把整个序列都计算出来并返回一个list
list(r)     # [1, 4, 9, 16, 25, 36, 49, 64, 81]

# 把list所有数字转为字符串
list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))     # ['1', '2', '3', '4', '5', '6', '7', '8', '9']





# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
# 序列求和，reduce实现
from functools import reduce
def add(x, y):
    return x + y
reduce(add, [1, 3, 5, 7, 9])    # 25

# 把序列[1, 3, 5, 7, 9]变换成整数13579
def fn(x, y):
    return x * 10 + y
reduce(fn, [1, 3, 5, 7, 9])     # 13579

# 字符串转整数
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s))