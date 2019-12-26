#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 将列表 [0,1,2,3.14,‘x’,None,’’,list(),{5}] 中各个元素转为布尔型
L = [0, 1, 2, 3.14, 'x', None, '', list(), {5}]
print([bool(item) for item in L])