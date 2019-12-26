#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 判断两个对象是在内存中是否是同一个
a = [1, 2]
b = a
print(id(b) == id(a))