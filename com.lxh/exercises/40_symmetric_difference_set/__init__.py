#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 返回两个集合 {‘A’,‘D’,‘B’} 和 {‘D’,‘E’,‘C’} 未重复的元素的集合
set1 = {'A', 'D', 'B'}
set2 = {'D', 'E', 'C'}
set3 = set1.symmetric_difference(set2)
print(set3)