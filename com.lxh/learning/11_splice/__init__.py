#!/usr/bin/env python3
# -*- coding: utf-8 -*-

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
# L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3
L[0:3]      # ['Michael', 'Sarah', 'Tracy']
# 如果第一个索引是0，还可以省略：
L[:3]       # 也可以从索引1开始，取出2个元素出来：
L[1:3]      # ['Sarah', 'Tracy']
L[-2:-1]    # ['Bob']

L = list(range(100))
# 前10个数，每两个取一个：
L[:10:2]    # [0, 2, 4, 6, 8]
# 所有数，每5个取一个：
L[::5]      # [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]

(0, 1, 2, 3, 4, 5)[:3]      # (0, 1, 2)

'ABCDEFG'[:3]       # 'ABC'
'ABCDEFG'[::2]      # 'ACEG'