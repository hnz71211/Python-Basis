#!/usr/bin/env python3
# -*- coding: utf-8 -*-

names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)


sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)


# [0, 1, 2, 3, 4]
list(range(5))


sum = 0
for x in range(101):
    sum = sum + x
print(sum)



# Python的for循环不仅可以用在list或tuple上，还可以作用在其他可迭代对象上

# dict迭代的是key。如果要迭代value，可以用for value in d.values(), 要同时迭代key和value，可以用for k, v in d.items()
# 字符串也是可迭代对象
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)

# 判断一个对象是可迭代对象
from collections import Iterable
isinstance('abc', Iterable) # str是否可迭代

# enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)