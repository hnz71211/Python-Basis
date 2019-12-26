#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 将二维结构 [[‘a’,1],[‘b’,2]] 和 ((‘x’,3),(‘y’,4)) 转成字典
L = [['a', 1], ['b', 2]]
T = (('x', 3), ('y', 4))

d1 = dict(L)
d2 = dict(T)
print(d1)
print(d2)