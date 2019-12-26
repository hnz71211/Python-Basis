#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 创建一个空集合，增加 {‘x’,‘y’,‘z’} 三个元素
# 使用大括号 { } 或者 set() 函数创建集合, 创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典
set = set()
set.update({'x', 'y', 'z'})
print(set)