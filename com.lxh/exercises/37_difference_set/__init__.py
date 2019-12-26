#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 返回集合 {‘A’,‘D’,‘B’} 中未出现在集合 {‘D’,‘E’,‘C’} 中的元素（差集）
set1 = {'A', 'D', 'B'}
set2 = {'D', 'E', 'C'}
set3 = set1.difference(set2)
set4 = set1 - set2
print(set3)
print(set4)