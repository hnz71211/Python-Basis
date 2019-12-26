#!/usr/bin/env python3
# -*- coding: utf-8 -*-

L = [[6, 5], [3, 7], [2, 8]]

# 根据每一行的首元素大小对二维列表 [[6, 5], [3, 7], [2, 8]] 排序
L1 = sorted(L, key=lambda x:x[0])   # key为小list的第一个元素，即x[0]; 默认reverse=False
print(L1)

# 根据每一行的尾元素大小对二维列表 [[6, 5], [3, 7], [2, 8]] 排序
L2 = sorted(L, key=lambda x:x[-1])  # key为小list的最后一个元素，即x[-1]; 设置reverse=True实现逆序
print(L2)