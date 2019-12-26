#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 将三个字符串 ‘15’, ‘127’, ‘65535’ 左侧补0成同样长度
L = ['15', '127', '65535']
len_max = max([len(item) for item in L])

for item in L:
    # Pad a numeric string with zeros on the left, to fill a field of the given width.
    print(item.zfill(len_max))