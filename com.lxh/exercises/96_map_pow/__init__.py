#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 使用 map 函数求列表 [2,3,4,5] 中每个元素的立方根
L = [item for item in map(lambda i: pow(i, 3), [2, 3, 4, 5])]
print(L)