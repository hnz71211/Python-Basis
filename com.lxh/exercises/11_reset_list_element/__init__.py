#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 将列表 [3,0,8,5,7] 中大于 5 元素置为1，其余元素置为0
L = [3, 0, 8, 5, 7]
for index, item in enumerate(L):
    if item > 5:
        L[index] = 1
    else:
        L[index] = 0
print(L)

# ----------------------------------------------

L = [1 if item > 5 else 0 for item in [3, 0, 8, 5, 7]]
print(L)