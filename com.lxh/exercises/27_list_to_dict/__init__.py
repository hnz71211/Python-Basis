#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 以列表 [‘A’,‘B’,‘C’,‘D’,‘E’,‘F’,‘G’,‘H’] 中的每一个元素为键，默认值都是0，创建一个字典
L = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
d = dict.fromkeys(L, 0)
print(d)