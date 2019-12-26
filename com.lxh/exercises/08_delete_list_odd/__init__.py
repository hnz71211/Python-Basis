#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 删除列表中索引号为奇数（或偶数）的元素
L1 = [True, 1, 0, 'x', None, 'x', False, 2, True]
del L1[::2]
print(L1)

L2 = [True, 1, 0, 'x', None, 'x', False, 2, True]
del L2[1::2]
print(L2)