#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 从列表 [1,4,7,2,5,8] 索引为3的位置开始，依次插入列表 ['w', 'x', 'y', 'z'] 的所有元素

L1 = [1, 4, 7, 2, 5, 8]
L2 = ['w', 'x', 'y', 'z']
for index, value in enumerate(L2):
    L1.insert(3 + index, value)
print(L1)

# -------------------------------------------

L1 = [1, 4, 7, 2, 5, 8]
L1[3:3] = ['w', 'x', 'y', 'z']   # 在索引为3的位置插入列表
print(L1)