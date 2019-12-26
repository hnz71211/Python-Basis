#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 从列表 [True,1,0,‘x’,None,‘x’,False,2,True] 中删除元素‘x’。
L = [True, 1, 0, 'x', None, 'x', False, 2, True]
for i in range(L.count('x')):
    L.remove('x')
print(L)