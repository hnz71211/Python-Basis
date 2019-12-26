#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# filter()也接收一个函数和一个序列。filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。

def is_odd(n):
    return n % 2 == 1
list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))    # [1, 5, 9, 15]

def not_empty(s):
    return s and s.strip()
list(filter(not_empty, ['A', '', 'B', None, 'C', '  ']))    # ['A', 'B', 'C']