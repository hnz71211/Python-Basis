#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 使用 sys.stdin.readline() 写一个和 input() 函数功能完全相同的函数
import sys
def my_input(prompt):
    print(prompt, end='')
    return sys.stdin.readline().strip()

str_input = my_input('请输入：')
print(str_input)