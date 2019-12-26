#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 将列表 [3,‘a’,5.2,4,{},9,[]] 中 大于3的整数或浮点数置为1，其余置为0
L = [1 if isinstance(item, (int, float)) and item > 3 else 0 for item in [3, 'a', 5.2, 4, {}, 9, []]]
print(L)