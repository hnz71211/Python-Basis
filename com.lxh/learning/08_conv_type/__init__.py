#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 类型转换
int('123')
int(12.34)
float('12.34')
str(1.23)
str(100)
bool(1)
bool('')

# 函数名其实就是指向一个函数对象的引用，
# 完全可以把函数名赋给一个变量，相当于给这个函数起了一个"别名"
a = abs
a(-1) #1