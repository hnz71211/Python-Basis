#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 判断两个集合 {‘A’,‘D’,‘B’} 和 {‘D’,‘E’,‘C’} 是否有重复元素
set1 = {'A', 'D', 'B'}
set2 = {'D', 'E', 'C'}
# isdisjoint()判断a和b是否不包含相同的元素，没有则返回true
set3 = not set1.isdisjoint(set2)
print(set3)