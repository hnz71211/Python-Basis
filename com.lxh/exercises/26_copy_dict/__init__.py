#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 若 a = dict()，令 b = a，执行 b.update({‘x’:1})， a亦被改变。为何？如何避免？
a = dict()
b = a
print(id(b) == id(a))

c = a.copy()
print(id(c) == id(a))