#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 找到列表 [8,5,2,4,3,6,5,5,1,4,5] 中出现最频繁的数字以及出现的次数
L = [8, 5, 2, 4, 3, 6, 5, 5, 1, 4, 5]
# key=L.count即给 每个元素调用L.count(i)函数
ele = max(set(L), key=L.count)
print(ele)
print(L.count(ele))