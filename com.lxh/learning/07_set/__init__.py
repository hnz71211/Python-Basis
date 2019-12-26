#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# set中没有重复的元素,无序
# 要创建一个set，需要提供一个list作为输入集合
s = set([1, 2, 3]) #{1, 2, 3}

s.add(4)

s.remove(4)

s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
s1 & s2 #{2, 3}
s1 | s2 #{1, 2, 3, 4}