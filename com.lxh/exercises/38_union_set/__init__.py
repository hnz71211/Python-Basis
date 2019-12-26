#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 返回两个集合 {‘A’,‘D’,‘B’} 和 {‘D’,‘E’,‘C’} 的并集
set1 = {'A', 'D', 'B'}
set2 = {'D', 'E', 'C'}
set3 = set1.union(set2)
print(set3)