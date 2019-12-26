#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 删除集合 {‘x’,‘y’,‘z’} 中的 ‘z’ 元素，增j加元素 ‘w’，然后清空整个集合
set = {'x', 'y', 'z'}
set.remove('z')
print(set)
set.add('w')
print(set)
set.clear()
print(set)