#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 清除字符串 ‘\t python \n’ 左侧、右侧，以及左右两侧的空白字符
s = '\t python \n'
print(s.lstrip())
print(s.rstrip())
print(s.strip())
