#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 将列表 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 拆分为奇数组和偶数组两个列表
L = list(range(10))
L1 = L[::2]
L2 = L[1::2]
print(L1)
print(L2)