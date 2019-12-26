#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

# 定义函数
def my_abs(x):
    # 数据类型的检查可以用内置函数isinstance()实现
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
my_abs(-9)

# 什么事也不做，可以用pass
def nop():
    pass


# 返回多个值, 实际上，函数返回的是一个tuple，语法上，tuple可以省略括号
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny