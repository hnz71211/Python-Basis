#!/usr/bin/env python3
# -*- coding: utf-8 -*-

list(range(1, 11))      # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

L = []
for x in range(1, 11):
    L.append(x * x)     # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

[x * x for x in range(1, 11)]       # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

[x * x for x in range(1, 11) if x % 2 == 0]     # [4, 16, 36, 64, 100]

[m + n for m in 'ABC' for n in 'XYZ']       # ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']

import os # 导入os模块，模块的概念后面讲到
[d for d in os.listdir('.')]  # os.listdir可以列出文件和目录

d = {'x': 'A', 'y': 'B', 'z': 'C'}
[k + '=' + v for k, v in d.items()]     # ['y=B', 'x=A', 'z=C']

L = ['Hello', 'World', 'IBM', 'Apple']
[s.lower() for s in L]      # ['hello', 'world', 'ibm', 'apple']

L = ['Hello', 'World', 18, 'Apple', None]
[s.lower() for s in L if isinstance(s, str)]