#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 若 a = [1,2,3]，令 b = a，执行 b[0] = 9， a[0]亦被改变。为何？如何避免？
a = [1, 2, 3]
b = a
print(id(a) == id(b))

c = a.copy()
print(id(c) == id(a))