#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import functools

# 2进制字符串转成10进制整数
def int2(x, base=2):
    return int(x, base)

# functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单
int2 = functools.partial(int, base=2)


#创建偏函数时，实际上可以接收函数对象、*args和**kw这3个参数

int2('10010')
# 相当于
# kw = { 'base': 2 }
# int('10010', **kw)


max2 = functools.partial(max, 10)
# 相当于
# args = (10, 5, 6, 7)
# max(*args)
# 实际上会把10作为*args的一部分自动加到左边
