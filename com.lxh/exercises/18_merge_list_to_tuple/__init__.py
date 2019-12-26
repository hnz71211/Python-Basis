#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 将列表 [‘x’,‘y’,‘z’] 和 [1,2,3] 转成 [(‘x’,1),(‘y’,2),(‘z’,3)] 的形式
L1 = ['x', 'y', 'z']
L2 = [1, 2, 3,4 ]


L = [(a, b) for a, b in zip(L1, L2)]
print(L)

for a, b in zip(L1, L2):
    print(a, b)